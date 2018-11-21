from selenium import webdriver
import time
import read
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

result=[]
dic = {
    '238':('_div50020306','_p50020306k50030306e10367','畅越冰激凌套餐238元国内流量不限量'),
    '128':('_div50020297','_p50020297k50030297e10367','畅越冰激凌套餐128元国内流量不限量'),
    '108':('_div50020295','_p50020295k50030295e10367','畅越冰激凌套餐108元国内流量不限量'),
    '118':('_div50020296','_p50020296k50030296e10367','畅越冰激凌套餐118元国内流量不限量'),
    '218':('_div50020305','_p50020305k50030305e10367','畅越冰激凌套餐218元国内流量不限量'),
    '98':('_div50020294','_p50020294k50030294e10367','畅越冰激凌套餐98元国内流量不限量'),
    '138':('_div50020298','_p50020298k50030298e10367','畅越冰激凌套餐138元国内流量不限量'),
    '148':('_div50020299','_p50020299k50030299e10367','畅越冰激凌套餐148元国内流量不限量'),
    '158':('_div50020300','_p50020300k50030300e10367','畅越冰激凌套餐158元国内流量不限量'),
    '168':('_div50020301','_p50020301k50030301e10367','畅越冰激凌套餐168元国内流量不限量'),
    '178':('_div50020302','_p50020302k50030302e10367','畅越冰激凌套餐178元国内流量不限量'),
    '188':('_div50020303','_p50020303k50030303e10367','畅越冰激凌套餐188元国内流量不限量'),
    '198':('_div50020304','_p50020304k50030304e10367','畅越冰激凌套餐198元国内流量不限量'),
    '258':('_div50020307','_p50020307k50030307e10367','畅越冰激凌套餐258元国内流量不限量'),
    '278':('_div50020308','_p50020308k50030308e10367','畅越冰激凌套餐278元国内流量不限量'),
    '298':('_div50020309','_p50020309k50030309e10367','畅越冰激凌套餐298元国内流量不限量'),
    '318':('_div50020310','_p50020310k50030310e10367','畅越冰激凌套餐318元国内流量不限量'),
    '358':('_div50020311','_p50020311k50030311e10367','畅越冰激凌套餐358元国内流量不限量'),
    '398':('_div50020312','_p50020312k50030312e10367','畅越冰激凌套餐398元国内流量不限量'),
    '48':('_div50020322','_p50020322k50030322e10367','畅越冰激凌套餐48元国内流量不限量'),
    '58':('_div50020323','_p50020323k50030323e10367','畅越冰激凌套餐58元国内流量不限量'),
    '68':('_div50020324','_p50020324k50030324e10367','畅越冰激凌套餐68元国内流量不限量'),
    '78':('_div50020325','_p50020325k50030325e10367','畅越冰激凌套餐78元国内流量不限量'),
    '88':('_div50020326','_p50020326k50030326e10367','畅越冰激凌套餐88元国内流量不限量'),
}
def login(driver):
    driver.find_element_by_id('STAFF_ID').clear()
    driver.find_element_by_id('STAFF_ID').send_keys('')
    driver.find_element_by_id('PASSWORD').send_keys('')
    driver.find_element_by_id('geneCode').click()
    vcode = input("verifyCode:")
    driver.find_element_by_id('SMS_VERIFY_CODE').send_keys(vcode)
    driver.find_element_by_id('bLoginSubmit').click()

    return driver

def to3G(driver,phone,people,tc):
    #查询号码
    driver.switch_to.default_content()
    driver.switch_to_frame('contentframe')
    driver.switch_to_frame('navframe_1')
    try:
        driver.find_element_by_css_selector("input[value=' 取消 ']").click()
    except Exception:
        pass
    driver.find_element_by_id('SERIAL_NUMBER').clear()
    driver.find_element_by_id('SERIAL_NUMBER').send_keys(phone)
    driver.find_element_by_id('queryTrade').click()
    time.sleep(2)
    for i in range(2):
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']").click()
        except Exception:
            pass
    time.sleep(2)
    #选套餐
    try:
        driver.find_element_by_id('baseProductList$dspl').click()
        driver.find_element_by_id('baseProductList$dspl').clear()
    except Exception:
        result.append(["失败","用户不存在或已停机或有未完成订单",phone])
        return driver
    # driver.execute_script("document.getElementById('baseProductList$dspl').setAttribute('value', '{}')".format(dic[tc][2]))
    # driver.find_element_by_id('baseProductList$dspl').click()
    driver.find_element_by_id('baseProductList$dspl').clear()
    driver.find_element_by_id('baseProductList$dspl').send_keys(dic[tc][2])
    driver.find_element_by_id('baseProductList$dspl').send_keys(Keys.ENTER)
    time.sleep(2)
    #判断是否存在冰淇淋套餐

    try:
        LTE=driver.find_element_by_xpath("//input[@id='{}']/../span[1]".format(dic[tc][1]))
    except Exception:
        try:
            bql=driver.find_element_by_xpath("//div[@id='{}']/span[1]".format(dic[tc][0]))
        except Exception:
            result.append(["失败","找不到套餐",phone])
            return driver
        if bql.get_attribute("style")=="COLOR: #f75000":
            result.append(["成功","",phone])
            return driver
        else:
            result.append(["失败","已存在其他冰淇淋套餐",phone])
            return driver
    #判断LTE服务是否选择
    if LTE.get_attribute("style")=="COLOR: blue":
        pass
    else:
        driver.find_element_by_id(dic[tc][1]).click()
    #填备注
    driver.find_element_by_id('REMARK').send_keys(people)
    driver.find_element_by_id('submitTrade').click()
    while(1):
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']")
            query=driver.find_elements_by_css_selector("input[value=' 确定 ']")
            for q in query[::-1]:
                q.click()
                try:
                    driver.switch_to.alert.accept()
                except Exception:
                    pass
            break
        except Exception as e:
            pass

    try:
        bottom=driver.find_elements_by_css_selector("input[value=' 确定 ']")
    except Exception:
        pass
    time.sleep(1)
    try:
        driver.switch_to_frame('feeframe')
        driver.find_element_by_id('continueTrade').click()
    except Exception:
        driver.switch_to.parent_frame()
        driver.find_element_by_id('submitTrade').click()
        while(1):
            try:
                driver.find_element_by_css_selector("input[value=' 确定 ']")
                break
            except Exception:
                pass
        text =driver.find_element_by_xpath("//input[@value=' 确定 ']/../preceding-sibling::div[1]").text
        result.append(["失败",text,phone])
        driver.find_element_by_css_selector("input[value=' 确定 ']").click()
        js="window.scrollTo(0,0)"
        driver.execute_script(js)
        time.sleep(1)
        return driver
    driver.find_element_by_css_selector("input[value=' 取消 ']").click()
    while(1):
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']").click()
            break
        except Exception:
            pass

    result.append(["成功","",phone])
    return driver

def qxdx(driver,phone,people,tc):
    driver.switch_to.default_content()
    driver.switch_to_frame('contentframe')
    driver.switch_to_frame('navframe_1')

    driver.find_element_by_id('SERIAL_NUMBER').clear()
    driver.find_element_by_id('SERIAL_NUMBER').send_keys(phone)
    driver.find_element_by_id('queryTrade').click()

    try:
        driver.find_element_by_css_selector("input[value=' 确定 ']").click()
        result.append(["成功","用户没有可取消的活动",phone])
        return driver
    except Exception:
        pass

    try:
        driver.find_element_by_xpath("//td[contains(text(),'{}')]".format(tc)).click()
    except Exception:
        result.append(["成功","没有需要取消的活动",phone])
        return driver

    try:
        driver.switch_to.alert.accept()
    except Exception:
        pass

    driver.find_element_by_id('REMARK').send_keys(people)
    driver.find_element_by_id('submitTrade').click()

    try:
        driver.switch_to.alert.accept()
    except Exception:
        pass

    time.sleep(2)
    driver.switch_to_frame('feeframe')
    driver.find_element_by_id('continueTrade').click()
    driver.find_element_by_css_selector("input[value=' 取消 ']").click()
    while(1):
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']").click()
            break
        except Exception:
            pass
    result.append(["成功","",phone])

    return driver

if __name__ == "__main__":
    driver= webdriver.Ie()
    driver.get('https://132.121.28.1/bssframe')
    input('wait')
    driver = login(driver)
    flag=input('点开我的收藏,并选择模式（0为3G转3G，1为取消低消）')
    phones, peoples,tcs = read.read("D:/自动受理数据.xlsx",flag)
    driver.switch_to_frame('sidebarframe')
    if flag=='0':
        driver.find_element_by_css_selector("a[value='产品变更']").click()
        driver.find_element_by_css_selector("a[value='产品变更']").click()
    else:
        driver.find_element_by_css_selector("a[value='合约计划取消']").click()
        driver.find_element_by_css_selector("a[value='合约计划取消']").click()
    total = len(phones)

    for i in range(1,total):
        try:
            if flag=='0':
                driver = to3G(driver,phones[i],peoples[i],tcs[i])
            else:
                driver = qxdx(driver,phones[i],peoples[i],tcs[i])
            now = len(result)
            print (now)
            print (result[now-1])
        except Exception as e:
            for r in result:
                print (r)
            read.write(result)
            print (e)
            print (phones[i])
            input('wait')
    for r in result:
        print (r)
    read.write(result)
    input('finished')
    driver.quit()
