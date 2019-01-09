

import requests
from bs4 import BeautifulSoup
import re,json

#获取财报三表的表头信息，生成json文件，供eastmoney_001.py调用

url = "http://emweb.securities.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=sz000004&type=web"
headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
        "Referer" : "http://data.eastmoney.com/yjfp/"
    }
resp = requests.get(url,headers = headers)
text = resp.text
# rr = re.compile(r'{{')
#text = re.sub("\{\{.*?\}\}",'',text,flags=re.S)
soup = BeautifulSoup(text,"lxml")
ids = ['zcfzb_qy','lrb_qy','xjllb_qy']
ids_tb = ['zcfzb_qy_tb','lrb_qy_tb','xjllb_qy_tb']
def get_refer(soup,id):
    refer = {}
    template = soup.find("script",id=id).prettify()  #将tag对象转化为str对象
    trs = re.findall("<tr>.*?</tr>",template,flags=re.S)
    for tr in trs:
        tds =  re.findall("<td.*?</td>",tr,flags=re.S)
        try:
            chs = re.search("<span>(&nbsp;)*(.*?)(</span>)",tds[0]).group(2)
            eng = re.search("\(value.(.*?),2\)",tds[1]).group(1)
            refer[eng] = chs
        except:
            pass
    return refer
def get_refer_tb(soup,id):
    refer = {}
    template = soup.find("script",id=id).prettify()  #将tag对象转化为str对象
    trs = re.findall("<tr>.*?</tr>",template,flags=re.S)
    for tr in trs:
        tds =  re.findall("<td.*?</td>",tr,flags=re.S)
        try:
            chs = re.search("<span>(&nbsp;)*(.*?)(</span>)",tds[0]).group(2)+"同比"
            eng = re.search("\(value.(.*?)\)",tds[1]).group(1)
            refer[eng] = chs
        except:
            pass
    return refer

refers = {}

for id in ids:
    refer = get_refer(soup,id)
    refers.update(refer)
for id in ids_tb:
    refer = get_refer_tb(soup, id)
    refers.update(refer)

print(refers)

with open("C:\\proj_stock\\eastmoney\\refer.json","w",encoding="utf-8") as fp:
    json.dump(refers,fp,ensure_ascii=False)



headers_zcfz = ['SECURITYCODE', 'REPORTTYPE', 'TYPE', 'REPORTDATE', 'MONETARYFUND', 'SETTLEMENTPROVISION', 'LENDFUND', 'FVALUEFASSET', 'TRADEFASSET', 'DEFINEFVALUEFASSET', 'BILLREC', 'ACCOUNTREC', 'ADVANCEPAY', 'PREMIUMREC', 'RIREC', 'RICONTACTRESERVEREC', 'INTERESTREC', 'DIVIDENDREC', 'OTHERREC', 'EXPORTREBATEREC', 'SUBSIDYREC', 'INTERNALREC', 'BUYSELLBACKFASSET', 'INVENTORY', 'CLHELDSALEASS', 'NONLASSETONEYEAR', 'OTHERLASSET', 'SUMLASSET', 'LOANADVANCES', 'SALEABLEFASSET', 'HELDMATURITYINV', 'LTREC', 'LTEQUITYINV', 'ESTATEINVEST', 'FIXEDASSET', 'CONSTRUCTIONPROGRESS', 'CONSTRUCTIONMATERIAL', 'LIQUIDATEFIXEDASSET', 'PRODUCTBIOLOGYASSET', 'OILGASASSET', 'INTANGIBLEASSET', 'DEVELOPEXP', 'GOODWILL', 'LTDEFERASSET', 'DEFERINCOMETAXASSET', 'OTHERNONLASSET', 'SUMNONLASSET', 'SUMASSET', 'STBORROW', 'BORROWFROMCBANK', 'DEPOSIT', 'BORROWFUND', 'FVALUEFLIAB', 'TRADEFLIAB', 'DEFINEFVALUEFLIAB', 'BILLPAY', 'ACCOUNTPAY', 'ADVANCERECEIVE', 'SELLBUYBACKFASSET', 'COMMPAY', 'SALARYPAY', 'TAXPAY', 'INTERESTPAY', 'DIVIDENDPAY', 'RIPAY', 'INTERNALPAY', 'OTHERPAY', 'ANTICIPATELLIAB', 'CONTACTRESERVE', 'AGENTTRADESECURITY', 'AGENTUWSECURITY', 'DEFERINCOMEONEYEAR', 'STBONDREC', 'CLHELDSALELIAB', 'NONLLIABONEYEAR', 'OTHERLLIAB', 'SUMLLIAB', 'LTBORROW', 'BONDPAY', 'PREFERSTOCBOND', 'SUSTAINBOND', 'LTACCOUNTPAY', 'LTSALARYPAY', 'SPECIALPAY', 'ANTICIPATELIAB', 'DEFERINCOME', 'DEFERINCOMETAXLIAB', 'OTHERNONLLIAB', 'SUMNONLLIAB', 'SUMLIAB', 'SHARECAPITAL', 'OTHEREQUITY', 'PREFERREDSTOCK', 'SUSTAINABLEDEBT', 'OTHEREQUITYOTHER', 'CAPITALRESERVE', 'INVENTORYSHARE', 'SPECIALRESERVE', 'SURPLUSRESERVE', 'GENERALRISKPREPARE', 'UNCONFIRMINVLOSS', 'RETAINEDEARNING', 'PLANCASHDIVI', 'DIFFCONVERSIONFC', 'SUMPARENTEQUITY', 'MINORITYEQUITY', 'SUMSHEQUITY', 'SUMLIABSHEQUITY', 'MONETARYFUND_YOY', 'SETTLEMENTPROVISION_YOY', 'LENDFUND_YOY', 'FVALUEFASSET_YOY', 'TRADEFASSET_YOY', 'DEFINEFVALUEFASSET_YOY', 'BILLREC_YOY', 'ACCOUNTREC_YOY', 'ADVANCEPAY_YOY', 'PREMIUMREC_YOY', 'RIREC_YOY', 'RICONTACTRESERVEREC_YOY', 'INTERESTREC_YOY', 'DIVIDENDREC_YOY', 'OTHERREC_YOY', 'EXPORTREBATEREC_YOY', 'SUBSIDYREC_YOY', 'INTERNALREC_YOY', 'BUYSELLBACKFASSET_YOY', 'INVENTORY_YOY', 'CLHELDSALEASS_YOY', 'NONLASSETONEYEAR_YOY', 'OTHERLASSET_YOY', 'SUMLASSET_YOY', 'LOANADVANCES_YOY', 'SALEABLEFASSET_YOY', 'HELDMATURITYINV_YOY', 'LTREC_YOY', 'LTEQUITYINV_YOY', 'ESTATEINVEST_YOY', 'FIXEDASSET_YOY', 'CONSTRUCTIONPROGRESS_YOY', 'CONSTRUCTIONMATERIAL_YOY', 'LIQUIDATEFIXEDASSET_YOY', 'PRODUCTBIOLOGYASSET_YOY', 'OILGASASSET_YOY', 'INTANGIBLEASSET_YOY', 'DEVELOPEXP_YOY', 'GOODWILL_YOY', 'LTDEFERASSET_YOY', 'DEFERINCOMETAXASSET_YOY', 'OTHERNONLASSET_YOY', 'SUMNONLASSET_YOY', 'SUMASSET_YOY', 'STBORROW_YOY', 'BORROWFROMCBANK_YOY', 'DEPOSIT_YOY', 'BORROWFUND_YOY', 'FVALUEFLIAB_YOY', 'TRADEFLIAB_YOY', 'DEFINEFVALUEFLIAB_YOY', 'BILLPAY_YOY', 'ACCOUNTPAY_YOY', 'ADVANCERECEIVE_YOY', 'SELLBUYBACKFASSET_YOY', 'COMMPAY_YOY', 'SALARYPAY_YOY', 'TAXPAY_YOY', 'INTERESTPAY_YOY', 'DIVIDENDPAY_YOY', 'RIPAY_YOY', 'INTERNALPAY_YOY', 'OTHERPAY_YOY', 'ANTICIPATELLIAB_YOY', 'CONTACTRESERVE_YOY', 'AGENTTRADESECURITY_YOY', 'AGENTUWSECURITY_YOY', 'DEFERINCOMEONEYEAR_YOY', 'STBONDREC_YOY', 'CLHELDSALELIAB_YOY', 'NONLLIABONEYEAR_YOY', 'OTHERLLIAB_YOY', 'SUMLLIAB_YOY', 'LTBORROW_YOY', 'BONDPAY_YOY', 'PREFERSTOCBOND_YOY', 'SUSTAINBOND_YOY', 'LTACCOUNTPAY_YOY', 'LTSALARYPAY_YOY', 'SPECIALPAY_YOY', 'ANTICIPATELIAB_YOY', 'DEFERINCOME_YOY', 'DEFERINCOMETAXLIAB_YOY', 'OTHERNONLLIAB_YOY', 'SUMNONLLIAB_YOY', 'SUMLIAB_YOY', 'SHARECAPITAL_YOY', 'OTHEREQUITY_YOY', 'PREFERREDSTOCK_YOY', 'SUSTAINABLEDEBT_YOY', 'OTHEREQUITYOTHER_YOY', 'CAPITALRESERVE_YOY', 'INVENTORYSHARE_YOY', 'SPECIALRESERVE_YOY', 'SURPLUSRESERVE_YOY', 'GENERALRISKPREPARE_YOY', 'UNCONFIRMINVLOSS_YOY', 'RETAINEDEARNING_YOY', 'PLANCASHDIVI_YOY', 'DIFFCONVERSIONFC_YOY', 'SUMPARENTEQUITY_YOY', 'MINORITYEQUITY_YOY', 'SUMSHEQUITY_YOY', 'SUMLIABSHEQUITY_YOY', 'CURRENCY']

with open("C:\\proj_stock\\eastmoney\\headers_zcfz.json","w",encoding="utf-8") as fp:
    json.dump(headers_zcfz,fp,ensure_ascii=False)

headers_lr = ['SECURITYCODE', 'REPORTTYPE', 'TYPE', 'REPORTDATE', 'TOTALOPERATEREVE', 'OPERATEREVE', 'INTREVE', 'PREMIUMEARNED', 'COMMREVE', 'OTHERREVE', 'TOTALOPERATEEXP', 'OPERATEEXP', 'INTEXP', 'COMMEXP', 'RDEXP', 'SURRENDERPREMIUM', 'NETINDEMNITYEXP', 'NETCONTACTRESERVE', 'POLICYDIVIEXP', 'RIEXP', 'OTHEREXP', 'OPERATETAX', 'SALEEXP', 'MANAGEEXP', 'FINANCEEXP', 'ASSETDEVALUELOSS', 'FVALUEINCOME', 'INVESTINCOME', 'INVESTJOINTINCOME', 'EXCHANGEINCOME', 'OPERATEPROFIT', 'NONOPERATEREVE', 'NONLASSETREVE', 'NONOPERATEEXP', 'NONLASSETNETLOSS', 'SUMPROFIT', 'INCOMETAX', 'NETPROFIT', 'COMBINEDNETPROFITB', 'PARENTNETPROFIT', 'MINORITYINCOME', 'KCFJCXSYJLR', 'BASICEPS', 'DILUTEDEPS', 'OTHERCINCOME', 'PARENTOTHERCINCOME', 'MINORITYOTHERCINCOME', 'SUMCINCOME', 'PARENTCINCOME', 'MINORITYCINCOME', 'TOTALOPERATEREVE_YOY', 'OPERATEREVE_YOY', 'INTREVE_YOY', 'PREMIUMEARNED_YOY', 'COMMREVE_YOY', 'OTHERREVE_YOY', 'TOTALOPERATEEXP_YOY', 'OPERATEEXP_YOY', 'INTEXP_YOY', 'COMMEXP_YOY', 'RDEXP_YOY', 'SURRENDERPREMIUM_YOY', 'NETINDEMNITYEXP_YOY', 'NETCONTACTRESERVE_YOY', 'POLICYDIVIEXP_YOY', 'RIEXP_YOY', 'OTHEREXP_YOY', 'OPERATETAX_YOY', 'SALEEXP_YOY', 'MANAGEEXP_YOY', 'FINANCEEXP_YOY', 'ASSETDEVALUELOSS_YOY', 'FVALUEINCOME_YOY', 'INVESTINCOME_YOY', 'INVESTJOINTINCOME_YOY', 'EXCHANGEINCOME_YOY', 'OPERATEPROFIT_YOY', 'NONOPERATEREVE_YOY', 'NONLASSETREVE_YOY', 'NONOPERATEEXP_YOY', 'NONLASSETNETLOSS_YOY', 'SUMPROFIT_YOY', 'INCOMETAX_YOY', 'NETPROFIT_YOY', 'COMBINEDNETPROFITB_YOY', 'PARENTNETPROFIT_YOY', 'MINORITYINCOME_YOY', 'KCFJCXSYJLR_YOY', 'BASICEPS_YOY', 'DILUTEDEPS_YOY', 'OTHERCINCOME_YOY', 'PARENTOTHERCINCOME_YOY', 'MINORITYOTHERCINCOME_YOY', 'SUMCINCOME_YOY', 'PARENTCINCOME_YOY', 'MINORITYCINCOME_YOY', 'CURRENCY']

with open("C:\\proj_stock\\eastmoney\\headers_lr.json","w",encoding="utf-8") as fp:
    json.dump(headers_lr,fp,ensure_ascii=False)

headers_xjll = ['SECURITYCODE', 'REPORTTYPE', 'TYPE', 'REPORTDATE', 'SALEGOODSSERVICEREC', 'NIDEPOSIT', 'NIBORROWFROMCBANK', 'NIBORROWFROMFI', 'PREMIUMREC', 'NETRIREC', 'NIINSUREDDEPOSITINV', 'NIDISPTRADEFASSET', 'INTANDCOMMREC', 'NIBORROWFUND', 'NDLOANADVANCES', 'NIBUYBACKFUND', 'TAXRETURNREC', 'OTHEROPERATEREC', 'SUMOPERATEFLOWIN', 'BUYGOODSSERVICEPAY', 'NILOANADVANCES', 'NIDEPOSITINCBANKFI', 'INDEMNITYPAY', 'INTANDCOMMPAY', 'DIVIPAY', 'EMPLOYEEPAY', 'TAXPAY', 'OTHEROPERATEPAY', 'SUMOPERATEFLOWOUT', 'NETOPERATECASHFLOW', 'DISPOSALINVREC', 'INVINCOMEREC', 'DISPFILASSETREC', 'DISPSUBSIDIARYREC', 'REDUCEPLEDGETDEPOSIT', 'OTHERINVREC', 'SUMINVFLOWIN', 'BUYFILASSETPAY', 'INVPAY', 'NIPLEDGELOAN', 'GETSUBSIDIARYPAY', 'ADDPLEDGETDEPOSIT', 'OTHERINVPAY', 'SUMINVFLOWOUT', 'NETINVCASHFLOW', 'ACCEPTINVREC', 'SUBSIDIARYACCEPT', 'LOANREC', 'ISSUEBONDREC', 'OTHERFINAREC', 'SUMFINAFLOWIN', 'REPAYDEBTPAY', 'DIVIPROFITORINTPAY', 'SUBSIDIARYPAY', 'BUYSUBSIDIARYPAY', 'OTHERFINAPAY', 'SUBSIDIARYREDUCTCAPITAL', 'SUMFINAFLOWOUT', 'NETFINACASHFLOW', 'EFFECTEXCHANGERATE', 'NICASHEQUI', 'CASHEQUIBEGINNING', 'CASHEQUIENDING', 'SALEGOODSSERVICEREC_YOY', 'NIDEPOSIT_YOY', 'NIBORROWFROMCBANK_YOY', 'NIBORROWFROMFI_YOY', 'PREMIUMREC_YOY', 'NETRIREC_YOY', 'NIINSUREDDEPOSITINV_YOY', 'NIDISPTRADEFASSET_YOY', 'INTANDCOMMREC_YOY', 'NIBORROWFUND_YOY', 'NDLOANADVANCES_YOY', 'NIBUYBACKFUND_YOY', 'TAXRETURNREC_YOY', 'OTHEROPERATEREC_YOY', 'SUMOPERATEFLOWIN_YOY', 'BUYGOODSSERVICEPAY_YOY', 'NILOANADVANCES_YOY', 'NIDEPOSITINCBANKFI_YOY', 'INDEMNITYPAY_YOY', 'INTANDCOMMPAY_YOY', 'DIVIPAY_YOY', 'EMPLOYEEPAY_YOY', 'TAXPAY_YOY', 'OTHEROPERATEPAY_YOY', 'SUMOPERATEFLOWOUT_YOY', 'NETOPERATECASHFLOW_YOY', 'DISPOSALINVREC_YOY', 'INVINCOMEREC_YOY', 'DISPFILASSETREC_YOY', 'DISPSUBSIDIARYREC_YOY', 'REDUCEPLEDGETDEPOSIT_YOY', 'OTHERINVREC_YOY', 'SUMINVFLOWIN_YOY', 'BUYFILASSETPAY_YOY', 'INVPAY_YOY', 'NIPLEDGELOAN_YOY', 'GETSUBSIDIARYPAY_YOY', 'ADDPLEDGETDEPOSIT_YOY', 'OTHERINVPAY_YOY', 'SUMINVFLOWOUT_YOY', 'NETINVCASHFLOW_YOY', 'ACCEPTINVREC_YOY', 'SUBSIDIARYACCEPT_YOY', 'LOANREC_YOY', 'ISSUEBONDREC_YOY', 'OTHERFINAREC_YOY', 'SUMFINAFLOWIN_YOY', 'REPAYDEBTPAY_YOY', 'DIVIPROFITORINTPAY_YOY', 'SUBSIDIARYPAY_YOY', 'BUYSUBSIDIARYPAY_YOY', 'OTHERFINAPAY_YOY', 'SUBSIDIARYREDUCTCAPITAL_YOY', 'SUMFINAFLOWOUT_YOY', 'NETFINACASHFLOW_YOY', 'EFFECTEXCHANGERATE_YOY', 'NICASHEQUI_YOY', 'CASHEQUIBEGINNING_YOY', 'CASHEQUIENDING_YOY', 'CURRENCY']

with open("C:\\proj_stock\\eastmoney\\headers_xjll.json","w",encoding="utf-8") as fp:
    json.dump(headers_xjll,fp,ensure_ascii=False)