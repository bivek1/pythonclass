nepali = {
    'apple': 'स्याउ',
    'banana': 'केरा',
    'chair': 'कुर्सी',
    'table': 'मेज',
    'computer': 'कम्प्युटर',
    'book': 'पुस्तक',
    'pen': 'कलम',
    'clock': 'घडी',
    'window': 'झ्याल',
    'door': 'ढोका',
    'car': 'गाडी',
    'bicycle': 'साइकल',
    'motorcycle': 'मोटरसाइकल',
    'plane': 'विमान',
    'train': 'रेल',
    'ship': 'नाव',
    'hat': 'टोपी',
    'shoes': 'जुत्ता',
    'shirt': 'कमीज',
    'pants': 'पायजामा',
    'socks': 'मोजा',
    'glasses': 'चश्मा',
    'umbrella': 'छाता',
    'phone': 'फोन',
    'television': 'टेलिभिजन',
    'radio': 'रेडियो',
    'bed': 'खाट',
    'lamp': 'बत्ती',
    'mirror': 'आईना',
    'knife': 'चाकू',
    'fork': 'काँटा',
    'spoon': 'चमचा',
    'plate': 'प्लेट',
    'cup': 'कप',
    'bowl': 'कटोरा',
    'pot': 'बर्तन',
    'pan': 'कराही',
    'brush': 'ब्रश',
    'soap': 'साबुन',
    'towel': 'तौलिया',
    'toothbrush': 'दाँतको ब्रश',
    'toothpaste': 'दाँतको पेस्ट',
    'shampoo': 'श्याम्पू',
    'conditioner': 'कंडिशनर',
    'bedroom': 'कोठा',
    'kitchen': 'भान्सा',
    'living room': 'बस्ती घर',
    'bathroom': 'बाथरूम',
    'garden': 'बगैचा',
    'school': 'विद्यालय',
    'hospital': 'अस्पताल',
    'bank': 'बैंक',
    'post office': 'डाकघर',
    'restaurant': 'भोजनालय'
}



print("\t\t\t Welcome to nepali dictionary")
search = input("What do you want to translate:").lower()

print(search)

print("The nepali translation of ", search , " is")

try:
    print(nepali[search])
except:
    print("Sorry there is no word like ", search , " in our dictionary")
# print(nepali.get(search))

# print(f"{search} this is english that is")