# captcha_breaker_selenium

Python script to perform automatically fill a captcha field in a selenium driver. 

This script uses OpenCV to pre-process and filter the captcha; It also uses tesseract as OCR engine to transform captcha in text. 

Below are some example of captchas, pre-processed captcha and output text:


![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/captchas/captchaa1.png)
![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/processed/processeda1.png)
![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/output/outputa1.png)

![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/captchas/captchaa6.png)
![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/processed/processeda6.png)
![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/output/outputa6.png)

![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/captchas/captchaa7.png)
![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/processed/processeda7.png)
![alt tag](https://raw.github.com/mmefenza/captcha_breaker_selenium/branch/output/outputa7.png)

The accurcay will depend on the type of captcha.

I noticed  that it works better when the characters do not touch each other in the captcha. The current accuracy was enough for the intended use. However, to improve it, i was thinking at

the following solution:

    1- Improve the training of the tesseract OCR engine with samples of the captchas targetted. One can find online tool to do the training of the tysseract OCR engine. 
    
    
    2- Use a set of different filters and morphological operations on the image and compare the different texts produced by OCR engine.
    
    
    3- Send the OCR engine output to a dictionnary or Google engine and analyze the the suggested corrections.