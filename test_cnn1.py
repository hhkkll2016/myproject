

import tushare as ts
import pandas as pd
import numpy as np
import datetime

import torch
from torch import nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.utils.data as Data
import torch.nn.functional as F
from torch.autograd import Variable


def pre_rnn_data(x,y):
    x = torch.FloatTensor(x)
    y = torch.LongTensor(y)
    #后|n|-1个数据作为测试集，前面的作为训练集
    n = -21
    x_train = x[:n,:]
    x_test = x[n:-1,:]
    y_train = y[:n,]
    y_test = y[n:-1,]
    print(x.size(),x_train.size(),x_test.size())
    print(y.size(), y_train.size(), y_test.size())
    # print(x_train)
    return x_train,y_train,x_test,y_test


def data_download(ts_code):
    end_date = datetime.datetime.now().strftime("%Y%m%d")
    end_date_a = datetime.datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.datetime.now() - datetime.timedelta(days=300)).strftime("%Y%m%d")
    start_date_a = (datetime.datetime.now() - datetime.timedelta(days=300)).strftime("%Y-%m-%d")
    api = ts.pro_api('411adaf2f9d94f98843cc8d37e96e1c86a849d763948375419d7e42f')
    #获取交易日历，并剔除非交易时间
    trade_cal = api.trade_cal(exchange='', start_date=start_date, end_date=end_date).sort_index(ascending=False)
    trade_cal = trade_cal[trade_cal['is_open']==1][1:]
    print(trade_cal)
    #获取某一只股票的信息
    df = ts.pro_bar(pro_api=api, ts_code=ts_code, adj='qfq', start_date=start_date, end_date=end_date)
    df.drop(['ts_code','trade_date','open','high','low','pre_close','change','amount'], axis=1, inplace=True)
    #获取指数信息
    close_hz300 = ts.get_h_data('000300', start=start_date_a, end=end_date_a,index=True)['close']
    close_cyb = ts.get_h_data('399006', start=start_date_a, end=end_date_a,index=True)['close']
    close_index = pd.concat([close_hz300,close_cyb],axis=1)
    close_index.columns = ['hz300','cyb']
    close_index.index = trade_cal['cal_date']
    #合并股票和指数数据,并删除有空的行
    data = close_index.join(df,how='outer')
    data.dropna(axis=0, how='any', inplace=True)
    # 转换数据为numpy
    # close_index = np.array(close_index)
    print(close_index)
    print(data)
    data.to_csv('2.csv')


def data_read():
    data = pd.read_csv('2.csv')
    data.drop(data.columns[0], axis=1, inplace=True)
    label_data = np.array(data['pct_chg'])
    label_data = labeltoonehot(label_data)
    data = np.array(data)
    #生成三维数组（批次号，序列长度，input输入长度，）
    n = len(data)
    x = np.zeros(shape=(n-TIME_STEP,TIME_STEP,5))
    y = np.zeros(shape=(n-TIME_STEP))
    # y_all = np.zeros(shape=(n-10,10,3))
    for i in range(n-TIME_STEP):
        x[i] = data[i:i+TIME_STEP]
        y[i] = label_data[i+TIME_STEP]
        # y_all[i] = label_data[i+1:i+11]
    # print(x)
    for index,i in enumerate(x):
        # 对data进行归一化处理0~1
        data_min = np.min(x[index], axis=0)  # 最小值
        data_max = np.max(x[index], axis=0)  # 最大值
        x[index] = (x[index] - data_min) / (data_max - data_min)
        # 对data进行标准化集中到-1~1
        data_mean = np.mean(x[index], axis=0)  # 均值
        data_std = np.std(x[index], axis=0)  # 标准差
        x[index] = (x[index] - data_mean) / data_std
        # print(x[index])
        # break
    # print(x.shape)
    # print(x)
    x = x.reshape(n-TIME_STEP, TIME_STEP*5)
    # print(x.shape)
    # print(x)
    return x,y


#生成类别标签数据格式
def labeltoonehot(pre_data):
    pre_data = pre_data.tolist()
    aa = []
    for a in pre_data:
        if a <= -2:
            aa.append(0)
        elif a > -2 and a <= 0:
            aa.append(1)
        elif a > 0 and a < 2:
            aa.append(2)
        elif a >= 2:
            aa.append(3)
    aa = np.array(aa)
    return aa


# 设置nn网络超参数
EPOCH = 130               # 设置全数据集训练的次数
BATCH_SIZE = 50             # 设置每次提取数量
TIME_STEP = 15          # 每次输入X数据的长度
INPUT_SIZE = 5         # 每个X数据的维度
LR = 0.01               # 学习率


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.hidden1 = torch.nn.Linear(75, 128)   # hidden layer
        # self.hidden2 = torch.nn.Linear(128, 64)  # hidden layer
        # self.hidden3 = torch.nn.Linear(64, 32)  # hidden layer
        self.predict = torch.nn.Linear(128, 4)   # output layer

    def forward(self, x):
        x = F.relu(self.hidden1(x))      # activation function for hidden layer
        # x = F.relu(self.hidden2(x))  # activation function for hidden layer
        # x = F.relu(self.hidden3(x))  # activation function for hidden layer
        out = self.predict(x)             # linear output
        return out

def main():
    # data_download("000651.SZ")
    x,y = data_read()
    x_train,y_train,x_test,y_test = pre_rnn_data(x,y)
    # 装载数据，将数据以元组（输入，标签）方式封装
    torch_dataset = Data.TensorDataset(x_train,y_train)
    # 按照批次取数据，每次随机取batch_size个数据
    train_loader = torch.utils.data.DataLoader(dataset=torch_dataset, batch_size=BATCH_SIZE, shuffle=True)

    # for i in train_loader:
    #     print(i)
    #     break

    net = Net()
    # print(net)


    optimizer = torch.optim.Adam(net.parameters(), lr=LR)  # optimize all nn parameters
    loss_func = nn.CrossEntropyLoss()  # the target label is not one-hotted
    # loss_func = nn.MultiLabelMarginLoss()
    # loss_func = nn.PoissonNLLLoss()
    for epoch in range(EPOCH):
        for step, (b_x, b_y) in enumerate(train_loader):  # gives batch data
            # print(b_x.size())
            output = net(b_x)  # rnn output
            # print(output)
            # print(b_y)
            # print(output.size())
            # print(b_y.size())
            loss = loss_func(output, b_y)  # cross entropy loss
            # print(loss)
            optimizer.zero_grad()  # clear gradients for this training step
            loss.backward()  # backpropagation, compute gradients
            optimizer.step()  # apply gradients
            # break
        # if step % 50 == 0:
        test_output = net(x_test)  # (samples, time_step, input_size)
        pred_y = torch.max(test_output, 1)[1].data.numpy()
        y_test1 = y_test.data.numpy()
        print(pred_y,y_test1)
        accuracy = float(sum((pred_y == y_test1).astype(int) == 1)) / float(y_test1.size)
        print('Epoch: ', epoch, '| train loss: %.4f' % loss.data.numpy(), '| test accuracy: %.2f' % accuracy)

        # break



def test():
    pass



if __name__ == '__main__':
    main()
    # test()