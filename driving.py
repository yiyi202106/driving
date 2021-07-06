country = input('請輸入您所屬的的國家：')
age = input('請輸入您的年齡：')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('你可以考駕照')
    else:
        print('你還不可以考駕照') 
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')
else:
	print('目前尚能查詢相關資訊')