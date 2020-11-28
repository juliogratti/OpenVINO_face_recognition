from deepface import DeepFace
result  = DeepFace.verify("img1.jpg", "img2.jpg")
#results = DeepFace.verify([['img1.jpg', 'img2.jpg'], ['img1.jpg', 'img3.jpg']])
print("Is verified: ", result["verified"])
