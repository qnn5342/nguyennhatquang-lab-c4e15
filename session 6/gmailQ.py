from gmail import GMail, Message
gmail = GMail('Quang <quangtechkid@gmail.com>','Techkid2403')
# msg = Message('Chao a Huy',to='xyz <c4e.201708@gmail.com>',text='having a new hair cut?')
html_template = '''<p>Hi anh Huy,</p>
<p>H&ocirc;m nay em mệt. Cho em nghỉ anh nh&eacute;</p>
<p>C&aacute;m ơn anh!!!</p>'''

msg = Message('Cho xin nghỉ học a Huy oi',to='Huy <c4e.201708@gmail.com>',html= html_template)
gmail.send(msg)
