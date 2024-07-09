from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .utils.AES import aes
from .utils.DES import des_extensions
from .utils.DES import des


# Create your views here.
def index(request):
    template = loader.get_template('input.html')
    context = {
        "message" : "",
        "error" : "",
    }
    return render(request, 'form_test_parameter.html', context)

def index2(request):
    template = loader.get_template('input.html')
    context = {
        "message" : "",
        "error" : "",
    }
    return render(request, 'form_test_parameter2.html', context)

def home(request):
    return render(request, 'index.html')


def validate_params(request):
    
    if request.method == 'POST':
        try:
            # Check if 2DES or 3DES
            des_type = request.POST.get('type')
            print(des_type)
            if des_type == '2DES':
                key1 = request.POST.get('key1')
                key2 = request.POST.get('key2')
                print(key1,key2)
                if str(key1) == key2:
                    print(key1, key2)
                    context = {
                        "error": "Pour 2DES, les clés doivent etre differentes",
                    }
                    return render(request, 'form_test_parameter.html', context)

                #raise ValueError("Pour 2DES, les clés doivent etre differentes.")
            elif des_type == '3DES':
                key1 = request.POST.get('key1')
                key2 = request.POST.get('key2')
                key3 = request.POST.get('key3')
                if key1 == key2 or key1 == key3 or key2 == key3:
                    context = {
                        "error": "Pour 3DES, les clés doivent etre differentes",
                    }
                    return render(request, 'form_test_parameter.html', context)

                    #raise ValueError("Pour 3DES, les clés doivent etre differentes.")
            else:
                key1 = request.POST.get('key1')

            plaintext = request.POST.get('message')
            process = request.POST.get('process')

            if process == 'encrypt':
                # Perform encryption based on DES type
                if des_type == '2DES':
                    # Handle 2DES encryption
                    d = des_extensions.DoubleDes(des.Des(),des.Des())
                    encrypted_text = d.encrypt(key1, key2, plaintext)
                    context = {
                        "id": 2,
                        "plaintext": plaintext,
                        "process": process,
                        "encrypted_text": encrypted_text,
                        "key": key1,
                        "key2": key2,
                    }
                elif des_type == '3DES':
                    # Handle 3DES encryption
                    d = des_extensions.TripleDes(des.Des(),des.Des(),des.Des())
                    encrypted_text = d.encrypt(key1,key2,key3,plaintext)
                    context = {
                        "id": 3,
                        "plaintext": plaintext,
                        "process": process,
                        "encrypted_text": encrypted_text,
                        "key": key1,
                        "key2": key2,
                        "key3": key3,
                    }
                else:
                    # Handle DES encryption
                    d = des.Des()
                    encrypted_text = d.encrypt(key1,plaintext)
                    context = {
                        "id" :1,
                        "plaintext": plaintext,
                        "process": process,
                        "encrypted_text": encrypted_text,
                        "key": key1
                    }

                return render(request, 'result.html', context)
            elif process == 'decrypt':
                # Perform encryption based on DES type
                if des_type == '2DES':
                    # Handle 2DES encryption
                    d = des_extensions.DoubleDes(des.Des(),des.Des())
                    decrypted_text = d.decrypt(key1, key2, plaintext)
                    context = {
                        "id": 2,
                        "plaintext": plaintext,
                        "process": process,
                        "decrypted_text": decrypted_text,
                        "key": key1,
                        "key2": key2,
                    }
                elif des_type == '3DES':
                    # Handle 3DES encryption
                    d = des_extensions.TripleDes(des.Des(),des.Des(),des.Des())
                    decrypted_text = d.decrypt(key1, key2, key3, plaintext)
                    context = {
                        "id": 3,
                        "plaintext": plaintext,
                        "process": process,
                        "decrypted_text": decrypted_text,
                        "key": key1,
                        "key2": key2,
                        "key3": key3,
                    }
                else:
                    # Handle DES encryption
                    d = des.Des()
                    decrypted_text = d.decrypt(key1, plaintext)
                    context = {
                        "id": 1,
                        "plaintext": plaintext,
                        "process": process,
                        "decrypted_text": decrypted_text,
                        "key": key1
                    }

                return render(request, 'result.html', context)
            else:
                # Perform encryption based on DES type
                if des_type == '2DES':
                    # Handle 2DES encryption
                    d = des_extensions.DoubleDes(des.Des(),des.Des())
                    encrypted_text = d.encrypt(key1, key2, plaintext)
                    decrypted_text = d.decrypt(key1, key2, encrypted_text)
                    context = {
                        "id": 2,
                        "plaintext": plaintext,
                        "process": process,
                        "decrypted_text": decrypted_text,
                        "encrypted_text": encrypted_text,
                        "encrypted_text_binary": des.string_to_bit_array(encrypted_text),

                        "key": key1,
                        "key2": key2,
                    }
                elif des_type == '3DES':
                    # Handle 3DES encryption
                    d = des_extensions.TripleDes(des.Des(),des.Des(),des.Des())
                    encrypted_text = d.encrypt(key1, key2, key3, plaintext)
                    decrypted_text = d.decrypt(key1, key2, key3, encrypted_text)
                    context = {
                        "id": 3,
                        "plaintext": plaintext,
                        "process": process,
                        "decrypted_text": decrypted_text,
                        "encrypted_text": encrypted_text,
                        "encrypted_text_binary": des.string_to_bit_array(encrypted_text),
                        "key": key1,
                        "key2": key2,
                        "key3": key3,
                    }
                else:
                    # Handle DES encryption
                    d = des.Des()
                    encrypted_text = d.encrypt(key1, plaintext)
                    decrypted_text = d.decrypt(key1, encrypted_text)
                    context = {
                        "id": 1,
                        "plaintext": plaintext,
                        "process": process,
                        "decrypted_text": decrypted_text,
                        "encrypted_text": encrypted_text,
                        "encrypted_text_binary" : des.string_to_bit_array(encrypted_text),
                        "key": key1
                    }

                return render(request, 'result.html', context)

            return render(request , 'form_test_parameter.html', context)

        except (ValueError , TypeError):
            print(TypeError,ValueError)
            context ={
                "error": "Other problem"
            }
            return render(request , 'form_test_parameter.html', context)

    else:
        
        pass


def validate_params_aes(request):
    if request.method == 'POST':
        try:
            # Check if 2DES or 3DES
            des_type = request.POST.get('type')
            print(des_type)
            key = request.POST.get('key')

            plaintext = request.POST.get('message')
            process = request.POST.get('process')


            plaintext_bytes = plaintext.encode('utf-8')
            key_bytes = key.encode('utf-8')
            print(key_bytes, len(key_bytes), plaintext_bytes)

            # Ensure key is 16, 24, or 32 bytes long for AES-128, AES-192, or AES-256 respectively
            if len(key_bytes) not in [16, 24, 32]:
                print("Key must be 16, 24, or 32 bytes long.")
                return

            # Ensure the data is a multiple of the block size by adding PKCS7 padding
            data = aes.add_padding(plaintext_bytes)

            # Perform encryption based on DES type

            # Perform AES encryption
            # Perform AES encryption on each block
            encrypted_blocks = [aes.aes_encryption(data[i:i + 16], key_bytes) for i in range(0, len(data), 16)]

            # Concatenate the encrypted blocks
            encrypted_data = b''.join(encrypted_blocks)
            print("Encrypted Data:", encrypted_data.hex())

            # Perform AES decryption on each block
            decrypted_blocks = [aes.aes_decryption(encrypted_data[i:i + 16], key_bytes) for i in
                                range(0, len(encrypted_data), 16)]

            # Concatenate the decrypted blocks
            decrypted_data = b''.join(decrypted_blocks)

            # Remove PKCS7 padding
            decrypted_data = aes.remove_padding(decrypted_data)

            decrypted_text = decrypted_data.decode('utf-8')
            print("Decrypted Text:", decrypted_text)



            if process == 'encrypt':
                context = {
                    "id": "AES",
                    "plaintext": plaintext,
                    "process": process,
                    "encrypted_text": encrypted_data,
                    "key": key,
                }

                return render(request, 'result.html', context)
            elif process == 'decrypt':
                context = {
                        "id": "AES",
                        "plaintext": plaintext,
                        "process": process,
                        "decrypted_text": decrypted_text,
                        "key": key,
                    }

                return render(request, 'result.html', context)
            else:

                context = {
                        "id": "AES",
                        "plaintext": plaintext,
                        "process": process,
                        "decrypted_text": decrypted_text,
                        "encrypted_text": encrypted_data,
                        "encrypted_text_binary": des.string_to_bit_array(encrypted_data),

                        "key": key,

                    }

                return render(request, 'result.html', context)

        except (ValueError, TypeError):
            print(TypeError, ValueError)
            context = {
                "error": "Other problem"
            }
            return render(request, 'form_test_parameter2.html', context)

    else:

        pass

        
        