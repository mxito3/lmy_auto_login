articleId = ""#此处为蓝墨云活动的id
courseId = "754182"#此处为蓝墨云的班级id
sleepNumber = 60#此值/60等于蓝墨云真实的做题用时时间
k = 30#此值代表随机选择试题的数量
URL_ROOT = r'https://www.mosoteach.cn/web/index.php?c=passport&m=account_login'#蓝墨云登陆提交地址
values = {
        'account_name': '13228210670',  # 此处为蓝墨云的账号
        'user_pwd': 'do25',  # 此处为蓝墨云的密码
        'remember_me': 'Y'  # 是否记住登陆状态，默认不记住
}
headers = {
        'Host': 'www.mosoteach.cn',
        'Accept-Encoding': 'gzip, deflate',
        'Origin': 'https://www.mosoteach.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.mosoteach.cn/web/index.php?c=passport&m=index',
}

subJectUrl = "https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=reply&clazz_course_id=" + courseId + "&id=" + articleId + "&order_item=group"