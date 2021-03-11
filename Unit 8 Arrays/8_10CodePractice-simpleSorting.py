vocab = ["Libraries", "Bandwidth", "Hierarchy", "Software", "Firewall", "Cybersecurity","Phishing", "Logic", "Productivity"]

print(vocab)
for i in range (len(vocab)-1):
    temp = vocab[i]
    sm = i + 1

    for j in range (i,len(vocab)):
        if (vocab[sm] > vocab [j]):
            sm = j
    vocab[i] = vocab[sm]
    vocab[sm] = temp
print(vocab)
