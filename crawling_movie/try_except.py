def TrygetText_xpath(element, path, default):
    try:
        result = element.find_element_by_xpath(path).text
    except:
        result = default
    return result

def TrygetText_id(element, path, default):
    try:
        result = element.find_element_by_id(path).text
    except:
        result = default
    return result
    
def TrygetAttribute(element, path, attr, default):
    try:
        result = element.find_element_by_xpath(path).get_attribute(attr)
    except:
        result = default
    return result

def TrygetStep5(element, path, default) :
    try:
        a= element.find_element_by_class_name('step5')
        dd =element.find_element_by_xpath(path).text
        try:
            result1 = int(dd.split('년')[0])
            if '/' not in dd:
                result2 = default
            else:
                result2 = dd.split('/')[-1].split(',')[0]
        except : 
            result1 = default
            result2 = dd.split(',')[0]
    except:
        result1 = default
        result2= default
    return result1, result2


def TrygetReopen(element, title) :

    l = len(element)
    if l == 4:
        n_reopen = len(element[3].text.split(',')) - 1
    elif l == 3 :
        try : 
            open_date = element[-1].find_element_by_xpath('.//a').text
            n_reopen = len(open_date.split(',')) -1
        except : 
            n_reopen = 0  # Conversion failed when converting the nvarchar value 'Null' to data type int.DB-Lib error message 20018, severity
            print('{0}는 영화 {1}의 상영시간인가? 그리고 개봉날짜가 없는가? 확인! '.format(element[-1].text,title))
    else:
        print('{0}는 span이 2개? 뭔지 확인!!!!!!!!!'.format(title))
        raise Exception
    return n_reopen