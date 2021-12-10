from agentocr import OCRSystem



ocr = OCRSystem(config='fa')
results = ocr.ocr('ouut.jpg')
for result in results:
    print(result)
    
    

