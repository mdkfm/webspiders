import requests

headers = {
	'Cookie': '_octo=GH1.1.1459855248.1667029097; logged_in=yes; preferred_color_mode=light; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; dotcom_user=mdkfm'}

r = requests.get('https://github.com/')
print(r.text)
