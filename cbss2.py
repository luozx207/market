# encoding:utf-8
from selenium import webdriver
import time
import read
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

result=[] #全局变量
dic = {'108':('_p90311370','_p90311370k51984422','showcolor90311370','_p90311370k51964227e5952770TD'),
       '138':('_p90343399','_p90343399k51984422','showcolor90343399','_p90343399k51976539e5952830TD'),
       '218':('_p90343406','_p90343406k51984422','showcolor90343406','_p90343406k51976546e5952970TD'),
       '238':('_p90343407','_p90343407k51984422','showcolor90343407','_p90343407k51976547e5952990TD'),
       '258':('_p90343408','_p90343408k51984422','showcolor90343408','_p90343408k51976548e5953010TD'),
       '98':('_p90311373','_p90311373k51984422','showcolor90311373','_p90311373k51964232e5952750TD'),
       '118':('_p90343397','_p90343397k51984422','showcolor90343397','_p90343397k51976537e5952790TD'),
       '128':('_p90343398','_p90343398k51984422','showcolor90343398','_p90343398k51976538e5952810TD'),
       '138':('_p90343399','_p90343399k51984422','showcolor90343399','_p90343399k51976539e5952830TD'),
       '148':('_p90343400','_p90343400k51984422','showcolor90343400','_p90343400k51976540e5952850TD'),
       '158':('_p90343401','_p90343401k51984422','showcolor90343401','_p90343401k51976541e5952870TD'),
       '168':('_p90343402','_p90343402k51984422','showcolor90343402','_p90343402k51976542e5952890TD'),
       '178':('_p90343403','_p90343403k51984422','showcolor90343403','_p90343403k51976543e5952910TD'),
       '188':('_p90343404','_p90343404k51984422','showcolor90343404','_p90343404k51976544e5952930TD'),
       '198':('_p90343405','_p90343405k51984422','showcolor90343405','_p90343405k51976545e5952950TD'),
       '278':('_p90343409','_p90343409k51984422','showcolor90343409','_p90343409k51976549e5953030TD'),
       '298':('_p90343410','_p90343410k51984422','showcolor90343410','_p90343410k51976550e5953050TD'),
       '318':('_p90343411','_p90343411k51984422','showcolor90343411','_p90343411k51976551e5953070TD'),
       '358':('_p90343412','_p90343412k51984422','showcolor90343412','_p90343412k51976552e5953090TD'),
       '398':('_p90343420','_p90343420k51984422','showcolor90343420','_p90343420k51976561e5953110TD'),
       '48':('_p90363849','','showcolor90363849','_p90363849k51999456e8351474TD'),
       '58':('_p90363850','','showcolor90363850','_p90363850k51999457e8351529TD'),
       '68':('_p90363851','','showcolor90363851','_p90363851k51999458e8351573TD'),
       '78':('_p90363852','','showcolor90363852','_p90363852k51999459e8351551TD'),
       '88':('_p90363853','','showcolor90363853','_p90363853k51999460e8351595TD'),
       '腾讯大王卡':('_p90063345','','showcolor90063345','')
       }

def login(driver):
    driver.find_element_by_id('STAFF_ID').send_keys('DSK32500')
    driver.find_element_by_id('LOGIN_PASSWORD').send_keys('aaaBBB8888')
    province=driver.find_element_by_id('LOGIN_PROVINCE_CODE')
    Select(province).select_by_value('51')
    vcode = input("verifyCode:")
    driver.find_element_by_id('VERIFY_CODE').send_keys(vcode)
    driver.find_element_by_xpath('//*[@class="submit clear"]/input[1]').click()

    SMS = input("SMS:")
    driver.find_element_by_css_selector("input[name='SMS_VERIFY_CODE']").send_keys(SMS)
    driver.find_element_by_id('bsubmit').click()

    return driver

def nav0(driver):
    input('change to 服务号码')
    driver.switch_to_frame('contentframe')
    driver.switch_to_frame('navframe_0')
    driver.switch_to_frame('chkcustframe')
    driver.find_element_by_id('SERIAL_NUMBER').send_keys('18565099490')
    driver.find_element_by_id('bssbutton').click()
    time.sleep(1)
    driver.switch_to.default_content()
    driver.switch_to_frame('sidebarframe')
    driver.find_element_by_css_selector("a[title='移网产品/服务变更']").click()
    return driver

def nav1(driver,tc,phone,people):
    driver.switch_to.default_content()
    driver.switch_to_frame('contentframe')
    driver.switch_to_frame('navframe_1')
    driver.find_element_by_id('SERIAL_NUMBER').clear()
    driver.find_element_by_id('SERIAL_NUMBER').send_keys(phone)
    #查询
    driver.find_element_by_id('queryTrade').click()
    #解决弹窗
    try:
        driver.find_element_by_css_selector("input[value=' 确定 ']").click()
    except Exception as e:
        pass
    time.sleep(2)

    #搜索套餐
    try:
        driver.find_element_by_id('queryProductName').send_keys(tc)
    except Exception:
        result.append(["失败","用户不存在或已停机或有未完成订单",phone])
        return driver
    driver.find_element_by_id('productNameQuery').click()
    time.sleep(0.5)
    #判断是否做过
    bql=driver.find_element_by_id(dic[tc][2])
    if bql.get_attribute("style")=="COLOR: #f75000":
        result.append(["成功","",phone])
        return driver
    #找到基本产品
    red=driver.find_elements_by_xpath("//span[contains(@style,'COLOR: red')]/span[1]")
    for r in red:
        if '基本产品' in r.text:
            r.find_element_by_xpath("./../preceding-sibling::input[1]").click()
            break
    try:
        driver.find_element_by_css_selector("input[value=' 确定 ']").click()
    except Exception:
        result.append(["失败","用户存在多个基础套餐",phone])
        js="window.scrollTo(0,0)"
        driver.execute_script(js)
        return driver

    #选套餐
    driver.find_element_by_id(dic[tc][0]).click()
    time.sleep(2)
    #对所有弹出选框选择确定(大王卡不知为何弹窗显示顺序跟源码相反)
    if dic[tc][3]:
        while(1):
            try:
                target=driver.find_element_by_css_selector("input[value=' 确定 ']")
                driver.execute_script("arguments[0].scrollIntoView();", target)
                target.click()
            except Exception as e:
                break
    else:
        query=driver.find_elements_by_css_selector("input[value=' 确定 ']")
        for q in query[::-1]:
            q.click()
    #如果已有冰淇淋套餐，这里会报错
    if dic[tc][3]:
        try:
            driver.find_element_by_id(dic[tc][3]).click()
        except Exception:
            result.append(["失败","已存在其他冰淇淋套餐",phone])
            return driver
    else:
        pass

    driver.find_element_by_id('REMARK').send_keys(people)
    driver.find_element_by_id('submitTrade').click()
    driver.find_element_by_css_selector("input[value=' 确定 ']").click()
    # wait1 = ui.WebDriverWait(driver,3)
    # #判断有无出错
    # try:
    #     wait1.until(lambda driver:driver.find_element_by_link_text("系统错误"))
    #     result.append(["失败","系统错误",phone])
    #     input("记录错误")
    #     driver.find_element_by_css_selector("input[value=' 确定 ']").click()
    #     return driver
    # except Exception as e:
    #     pass
    if dic[tc][3]:
        while(1):
            try:
                text =driver.find_element_by_xpath("//input[@value=' 确定 ']/../preceding-sibling::div[1]").text
                if "温馨提示" in text:
                    driver.find_element_by_css_selector("input[value=' 确定 ']").click()
                    break
                else:
                    result.append(["失败",text,phone])
                    driver.find_element_by_css_selector("input[value=' 确定 ']").click()
                    js="window.scrollTo(0,0)"
                    driver.execute_script(js)
                    time.sleep(1)
                    return driver
            except Exception as e:
                pass
    else:
        time.sleep(4)
        try:
            text =driver.find_element_by_xpath("//input[@value=' 确定 ']/../preceding-sibling::div[1]").text
            if "温馨提示" in text:
                driver.find_element_by_css_selector("input[value=' 确定 ']").click()
            else:
                result.append(["失败",text,phone])
                driver.find_element_by_css_selector("input[value=' 确定 ']").click()
                js="window.scrollTo(0,0)"
                driver.execute_script(js)
                time.sleep(1)
                return driver
        except Exception as e:
            pass
    time.sleep(1)
    driver.switch_to_frame('feeframe')
    driver.find_element_by_id('continueTrade').click()

    time.sleep(1)
    while(1):
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']").click()
        except Exception as e:
            break
    time.sleep(1)
    try:
        driver.switch_to.alert.dismiss()
    except Exception:
        pass

    result.append(["成功","",phone])

    return driver

#取消低消
def nav3(driver,phone,people):
    driver.switch_to.default_content()
    driver.switch_to_frame('contentframe')
    driver.switch_to_frame('navframe_1')
    driver.find_element_by_id('SERIAL_NUMBER').clear()
    driver.find_element_by_id('SERIAL_NUMBER').send_keys(phone)
    #查询
    driver.find_element_by_id('queryTrade').click()
    #解决弹窗
    try:
        driver.find_element_by_css_selector("input[value=' 确定 ']").click()
    except Exception as e:
        pass
    time.sleep(2)

    red=driver.find_elements_by_xpath("//span[contains(@style,'COLOR: red')]/span[1]")
    for r in red:
        if '低消' in r.text:
            r.find_element_by_xpath("./../preceding-sibling::input[1]").click()
            break
    else:
        result.append(["失败","找不到低消套餐",phone])
        js="window.scrollTo(0,0)"
        driver.execute_script(js)
        return driver

    driver.find_element_by_id('REMARK').send_keys(people)
    driver.find_element_by_id('submitTrade').click()
    driver.find_element_by_css_selector("input[value=' 确定 ']").click()

    driver.switch_to_frame('feeframe')
    while(1):
        try:
            driver.find_element_by_id('continueTrade').click()
            break
        except Exception:
            pass
    time.sleep(1)
    while(1):
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']").click()
        except Exception as e:
            break
    time.sleep(1)
    try:
        driver.switch_to.alert.dismiss()
    except Exception:
        pass

    result.append(["成功","",phone])

    return driver

dict2={
    '48':('畅越冰激凌国内不限流量套餐-48元档'),
    '98':('畅越冰激凌国内不限流量套餐-98元档'),
    '178':('畅越冰激凌国内不限流量套餐-178元档'),
    '218':('畅越冰激凌国内不限流量套餐-218元档'),
    '278':('畅越冰激凌国内不限流量套餐-278元档'),
    '108':('畅越冰激凌国内不限流量套餐-108元档'),
    '168':('畅越冰激凌国内不限流量套餐-168元档'),
    '188':('畅越冰激凌国内不限流量套餐-188元档'),
    '158':('畅越冰激凌国内不限流量套餐-158元档'),

}

def nav2(driver,tc,phone,people):
    driver.switch_to.default_content()
    driver.switch_to_frame('contentframe')
    driver.switch_to_frame('navframe_1')

    driver.find_element_by_id('netTypeCodeOld$dspl').click()
    driver.find_element_by_id('netTypeCodeOld$dspl').clear()
    driver.find_element_by_id('netTypeCodeOld$dspl').send_keys('GSM移动业务')
    driver.find_element_by_id('netTypeCodeOld$dspl').send_keys(Keys.ENTER)

    driver.find_element_by_id('SERIAL_NUMBER').clear()
    driver.find_element_by_id('SERIAL_NUMBER').send_keys(phone)
    driver.find_element_by_id('queryTrade').click()

    while(1):
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']").click()
            break
        except Exception:
            pass

    driver.find_element_by_id('policebutton').click()
    al=driver.switch_to.alert
    if '身份证号码不能为空' in al.text:
        al.accept()
        result.append(["失败","查询失败",phone])
        return driver
    time.sleep(2)
    old_handle = driver.current_window_handle
    print (len(driver.window_handles))
    for handle in driver.window_handles:
        if handle!=old_handle:
            driver.switch_to_window(handle)
            driver.switch_to_frame('contentframe')
            f= open('1.html','w')
            f.write(driver.page_source)
            f.close()
            try:
                driver.find_elements_by_css_selector("input[value=' 确定 ']").click()
            except Exception:
                pass
            driver.find_element_by_id('read').click()
            time.sleep(0.5)
            driver.find_element_by_css_selector("input[value='确 定']").click()

    input('wait')

    driver.find_element_by_id('productName').send_keys(dict2[tc][0])
    driver.find_element_by_id('btnQryProdByName').click()
    driver.find_element_by_id('prodType').click()

if __name__ == "__main__":

    driver= webdriver.Ie()
    driver.get('http://cbss.10010.com/')
    driver = login(driver)
    flag = input('请选择方法（0为4G转4G，1为2/3G转4G，2为取消低消）')
    phones, peoples, tcs= read.read("D:/自动受理数据.xlsx",'0')
    if flag=='1':
        driver.switch_to_frame('sidebarframe')
        driver.find_element_by_css_selector("a[value='2/3G转4G']").click()
    else:
        driver = nav0(driver)

    time.sleep(1)
    total = len(phones)
    for i in range(1,total):
        try:
            if flag=='0':
                driver = nav1(driver,tcs[i],phones[i],peoples[i])
            elif flag=='1':
                driver = nav2(driver,tcs[i],phones[i],peoples[i])
            elif flag=='2':
                driver = nav3(driver,phones[i],peoples[i])
            now = len(result)
            print (now)
            print (result[-1])
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
