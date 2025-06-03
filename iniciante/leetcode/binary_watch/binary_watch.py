

def readBinaryWatch(turnedOn):
    
    bits = [
        ("m-1", 1),
        ("m-2", 2),
        ("m-4", 4),
        ("m-8", 8),
        ("m-16", 16),
        ("m-32", 32),
        ("h-1", 1),
        ("h-2", 2),
        ("h-4", 4),
        ("h-8", 8),
    ]


    output = []

    def bt(partial, index):

        if len(partial) == turnedOn:
            
            h = 0
            m = 0
            for chave, valor in partial:
                if chave.startswith("h-"):
                    h += valor
                else:
                    m += valor
            
            if h <= 11 and m <= 59:
                m_str = f"0{m}" if m < 10 else m

                output.append(f"{h}:{m_str}")

                
        else:  
            for i in range(index, len(bits)):
                partial.append(bits[i])
                bt(partial, i + 1)
                partial.pop()

                  
                 
    bt([], 0)
    return output


print(*readBinaryWatch(1))

