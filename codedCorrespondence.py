alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

text = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx"
offset = 7


## Decoding function
def decoding_caesar(text, offset):
    message = ""
    for i in text:
        index = alphabet.find(i) + offset
        letter = alphabet[index]
        message += letter
    space = alphabet[(offset - 1)]
    print(message.replace(space, " "))

## Encoding function
def encoding_caesar(reply, offset):
    coded_reply = ""
    for i in reply:
        reply.strip(" ")
        index = alphabet.find(i) - offset
        letter = alphabet[index]
        coded_reply += letter
    print(coded_reply)



coded_message = " txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "sdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirfsdneirf"
####Viginere decoding

coded_message.strip("!").strip("?")

def decoding(coded_message, keyword):
    decoded_reply = ""
    for idx, i in enumerate(coded_message):
        index = alphabet.find(i) + alphabet.index(keyword[idx])
        letter = alphabet[index]
        decoded_reply += letter
    print(decoded_reply)

