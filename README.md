# captcha_breaker_selenium

Python script to automatically fill a captcha field in a selenium driver. 

This script uses OpenCV to pre-process and filter the captcha; It also uses tesseract as OCR engine to transform captcha in text. 

The accurcay will depend on the type of captcha. I noticed  that it works better when the characters do not touch each other in the captcha. The current accuracy was enough for the intended use. However, to improve it, i was thinking at

the following solutions:

    1- Improve the training of the tesseract OCR engine with samples of the captchas targetted. One can find online tool to do the training of the tysseract OCR engine. 
    
    
    2- Use a set of different filters and morphological operations on the image and compare the different texts produced by OCR engine.
    
    
    3- Send the OCR engine output to a dictionnary or Google engine and analyze the the suggested corrections.


Below are some example of captchas, pre-processed captcha and output text:

 Captcha   | pre-processed   | output
 
 
![Captcha](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/captchas/captchaa1.png)

![pre-processed](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/processed/processeda1.png)

![output](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/output/outputa1.png)

![Captcha](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/captchas/captchaa6.png)

![pre-processed](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/processed/processeda6.png)

![output](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/output/outputa6.png)

![Captcha](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/captchas/captchaa7.png)

![pre-processed](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/processed/processeda7.png)

![output](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/output/outputa7.png)

![Captcha](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/captchas/captchaa4.png)

![pre-processed](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/processed/processeda4.png)

![output](https://raw.githubusercontent.com/mmefenza/captcha_breaker_selenium/master/output/outputa4.png)
