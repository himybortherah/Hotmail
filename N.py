import requests

cookies = {
    'buid': '1.AV0AMe_N-B6jSkuT5F9XHpElWgIAAAAAAPEPzgAAAAAAAAABAABdAA.AQABGgEAAABVrSpeuWamRam2jAF1XRQE4TMok4JoAJ6l7CatPRurahxD7AqX_DPpxcdhZSC0gRfR1gcFwdkw1_SYkZN8Jbv18mPV7JypkJ9padbMD03klWN16J-_wH32QMwj07-ziKMgAA',
    'esctx': 'PAQABBwEAAABVrSpeuWamRam2jAF1XRQEbZPnsKAccT5AzH6wUYlyQoIMuYweyX_DZavQ1VD5D8ey_MNpW3vgeIxoF4jCVwer0PHH8i_kEG5iKm2oqaWe7aiVEAze7ozry3o2jrXeP9H6PER53GVmmELTpuC2_vzGQZ5QUMWyQQWxl1qlIuIKv1W03z-fsz6qkzuuxc1OaIsgAA',
    'esctx-7J51iFkczlw': 'AQABCQEAAABVrSpeuWamRam2jAF1XRQEXWsZ6m4lzwmqur6wPqSAYBjujpqQ2PgFcF4EJdI2hH4Ou3VwwP3a54v8IKoLrEG6kKHUVZajmJFqB7E-rCkoI9nGxegqmLCp4tqozWy8jEyflUUwBegEzHWgF_ITKfXHKJdBM38bDPUmlbM-qsiqLyAA',
    'fpc': 'AhEF1SK436dGjO-JOu28ljWerOTJAQAAAEHWdN8OAAAA',
    'x-ms-gateway-slice': 'estsfd',
    'stsservicecookie': 'estsfd',
    'MicrosoftApplicationsTelemetryDeviceId': '57b3f074-df80-45a1-8661-0bcb2f6a33e0',
    'brcap': '1',
    'ai_session': 'EniZeP4RK91LmCpd7OUsli|1742921556975|1742921556975',
}

headers = {
    'authority': 'login.microsoftonline.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'canary': 'PAQABDgEAAABVrSpeuWamRam2jAF1XRQEHPK3DbfGb_s2_jnnSYV0ClhKZ29PF3yYxQoPp5wkPWLs1gTjJhUt4mIk0EU9AFhZDb9R4bLiICB98uPbb2rqj3OfCVAWtKl_l-p6tyfA28DAv0pT8fH6iKdqXS-rN0xy-cjAUAPGbEkqNjfTBumqtc2JJbOUWP6EMxl4E39G13ujkIDe1_Nhbmwwhr2dk-7wavlufNWyNEjRx9fJO-cSfSAA',
    'client-request-id': '77fd21ed-3f4c-fcd2-0dab-7a952644744d',
    'content-type': 'application/json; charset=UTF-8',
    # 'cookie': 'buid=1.AV0AMe_N-B6jSkuT5F9XHpElWgIAAAAAAPEPzgAAAAAAAAABAABdAA.AQABGgEAAABVrSpeuWamRam2jAF1XRQE4TMok4JoAJ6l7CatPRurahxD7AqX_DPpxcdhZSC0gRfR1gcFwdkw1_SYkZN8Jbv18mPV7JypkJ9padbMD03klWN16J-_wH32QMwj07-ziKMgAA; esctx=PAQABBwEAAABVrSpeuWamRam2jAF1XRQEbZPnsKAccT5AzH6wUYlyQoIMuYweyX_DZavQ1VD5D8ey_MNpW3vgeIxoF4jCVwer0PHH8i_kEG5iKm2oqaWe7aiVEAze7ozry3o2jrXeP9H6PER53GVmmELTpuC2_vzGQZ5QUMWyQQWxl1qlIuIKv1W03z-fsz6qkzuuxc1OaIsgAA; esctx-7J51iFkczlw=AQABCQEAAABVrSpeuWamRam2jAF1XRQEXWsZ6m4lzwmqur6wPqSAYBjujpqQ2PgFcF4EJdI2hH4Ou3VwwP3a54v8IKoLrEG6kKHUVZajmJFqB7E-rCkoI9nGxegqmLCp4tqozWy8jEyflUUwBegEzHWgF_ITKfXHKJdBM38bDPUmlbM-qsiqLyAA; fpc=AhEF1SK436dGjO-JOu28ljWerOTJAQAAAEHWdN8OAAAA; x-ms-gateway-slice=estsfd; stsservicecookie=estsfd; MicrosoftApplicationsTelemetryDeviceId=57b3f074-df80-45a1-8661-0bcb2f6a33e0; brcap=1; ai_session=EniZeP4RK91LmCpd7OUsli|1742921556975|1742921556975',
    'hpgact': '1800',
    'hpgid': '1104',
    'hpgrequestid': '1d5f63ca-2d05-42ab-a77f-db6ad67e5800',
    'origin': 'https://login.microsoftonline.com',
    'referer': 'https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&nonce=638785183363501722.dac79284-2707-41ca-a3bf-0b187dd93c78&msaredir=1&client-request-id=77fd21ed-3f4c-fcd2-0dab-7a952644744d&protectedtoken=true&claims=%7b%22id_token%22%3a%7b%22xms_cc%22%3a%7b%22values%22%3a%5b%22CP1%22%5d%7d%7d%7d&prompt=select_account&state=TY3BboJAGITVvos36s_-4C4H0jS11jaCFRYVLmbZxagVJbiK8Hp9sXLQpIdvMnOYmW6n03lq6bV0oZUOHSKjzDYZ4hBtMCkhz0pI6hBmGYQCNSxTCkNgujEgNRlVykFJWbft_vYGp0oMXorylBfaPWeHTOq1kPJ0Oeq-kDqstKvLS3b3vC4yF-4hLKU7zICCbTkGxU17BEoawhbEwFQxicJymHh0Qy1Kzc-uSS3iENNGBBP7Zy105pr9MlO7sj3nJ1dMApATbzitnataBeeUOOU0d_IkP-yT0N6nBK7pclykb2wdL32IUMH3KqjVMsofeTE5VAmH6isf79XYx5Y6boAk_BW9UQSzENAjMU75vEo-PB3zxdbbQRPncytu_K0_-rHif3sRBlt5DCLZwM1v5vWMf9587jXe6L35Aw',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

params = {
    'mkt': 'en-US',
}

json_data = {
    'username': 'joe@hotmail.com',
    'isOtherIdpSupported': True,
    'checkPhones': True,
    'isRemoteNGCSupported': True,
    'isCookieBannerShown': False,
    'isFidoSupported': True,
    'originalRequest': 'rQQIARAAjZI7jNt0AMbj5C5whban7ggRIYaCL_7Hz0SqkO3k4jycOBfniZDlvx-Jn38ndl6uDlbGLgwgsTCAdF0qJujEfNOJocOxdKxOAiEWOlCpd2Jhg9_w6Zu-4dPvfg4cgcr7xD-U8JvECdsGuGHdtH-xvHfr8Lf3Xm3aH__y9-3H6ZcfVBP5DHt3niRRXCkW0SrxEfKOkG07hnVkoKCINnrxRwy7wLAXGHaWZRmSYzkacCTJkDQB2FLpyNQNtlziKLzEEixOAUPHdRLaOAEBx5pmmTRY7jJ7t8uvknnpJtDSSa2r7J3Y8i0j0XTDQKsw-TN7YKNloEUoTr7OfZdTJ6QAUZOvN9ThGsUkE2s4JVIS4fYBcHXx-GQybAdwutVnwyZ0WpwUleNxuxc1zLUcdifBiAkJ0l8wcEig6aAr9VtuWp1MqbmQyKI3T4mowcyFoD7piZ3-VhW9zmzl1madE3-4846bI2gn2npSjwgkj9Fy5wu2rowsSe0ugKc0ia61wL3qIk5a63afhORapHbHODVvtwZs2hBFqHr17QCwQg3pmzmsbY57W8do7gJpTvR2oJUa-KrfJ51ap1MXBIWd7gBBR8uy7HfZ2CXDJjBlPuJVmDpJqCe6YFmDbndAmFrDU_CdSnSYUGixkeHvPFjamG2y1BjIEtlauEM5Rral1ughH0iME9tseTzZ0hMGIt7ThFF50OuntQ7vygOWXtcQrghkujUh7J0oobFLVlqL0PCl5NhkfCL4CV0V29ONDNb0eiTbZZpj3bHFtEma35zl_pd4P-Ty1zYFKDzP5VFkhY55sYc938Ou9rIE9nIP-3b_2sxzQ3tnH38sfP_5r-6zz8aZ8_0i21lGLhhwHK0QcTzrw8huwrItVSO6V_c-BLxenSn1hRJx_AOmAh7lsUf5_NP8wZu5w0whJyrgRR77I4998Ubm6cF_aX7xFnb5NnUrb_i6E8T37j8sOKaWIM8KC5WHhW0Qa4Zx09a6v7LiQuWTwvV-4dPT09Ofb2de3vnmyVc_Pfvr8nfp6u5HqwiYapOWF_7K7cCymlzfCGdVSDnjqFFPg8UkClrqvCosjAdPDjPPDzOvAQ2',
    'country': 'DZ',
    'forceotclogin': False,
    'isExternalFederationDisallowed': False,
    'isRemoteConnectSupported': False,
    'federationFlags': 0,
    'isSignup': False,
    'flowToken': 'AQABIQEAAABVrSpeuWamRam2jAF1XRQEC0BwSPdWmYtrnZoux-YtEn8tuxtcd_skGeX4R8P9GyvsUjXMQISZW9RwZ0tWHmGDNsTM6tPqQ9HGSB9K4kG-_JTqjlLh6ax-8igU9OhF94pBgUVV2d4jk1brPqDbdLQGTykIconnrlNxrSSTI0mU_ufdd5NNG_Uvau9EZax5Wwy7Yxs6hYVr-IiCyiLcdE0sENbM-URxH2TbbxEmBHUZFdhspQxU64-_2VDrIqNOZ40I-aBkrRABf2793SyRQQMzi7lQv9KHjHLd9QTtD8CtsxNDtH_wb7xQow7SJ7NsxA2jPYV7D9oHDB7rLAurC8MlBkbUTITLzSaqf-JxPadjQonS543SZ3ItubrdynrWffEDXfi3spldiJ6VrFFjWzzolHdXU_KPaE74zXb-gSjLmI43NxwqfkWf2XcIWcKcj45YP_YEaURt0juDe1WRGZE5gMnYw6xIdHLojROPsodB8YDX64QQfAQri3tkKLA-8hC5f0EHzaj30IP0FCZqOYvKIAA',
    'isAccessPassSupported': True,
    'isQrCodePinSupported': True,
}

response = requests.post(
    'https://login.microsoftonline.com/common/GetCredentialType',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
).text
print(response)
if '"IfExistsResult":1' in response:
	print(True)
