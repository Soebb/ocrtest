from agentocr import OCRSystem



ocr = OCRSystem(config='fa')
results = ocr.ocr('out.jpg')
for result in results:
    print(result)
    
    

