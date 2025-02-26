from dataclasses import dataclass

HOME_DIRECTORY = r"C:/Users/Holly/Downloads/"

def GC_content(dna_seq: str) -> float:
    lenDNA = len(dna_seq)
    countGC = dna_seq.count("G") + dna_seq.count("C")
    return countGC / lenDNA


def get_file(filename: str):
    return open((HOME_DIRECTORY + filename), "r")

def list_to_str(list_obj: list, delimit: str = "") -> str:
    final_output = delimit.join([str(nums) for nums in list_obj])
    return final_output

def str_to_nums(input: str, delimit: str = " ") -> list[int]:
    num_list = list(map(int, input.split(delimit)))
    return num_list


@dataclass
class FastaInstance:
    name: str
    dna: str


def read_fasta(filename: str) -> list[FastaInstance]:
    
    read_in = get_file(filename).readlines()

    fasta_list = []
    dna_concat = []

    for i in range(len(read_in)):
        if read_in[i][0] == ">":
            if i != 0:
                dna = "".join(dna_concat)
                new_entry = FastaInstance(name, dna)
                fasta_list.append(new_entry)
                dna_concat = []
            name = read_in[i].replace("\n","").replace(">","")
        else:
            dna_concat.append(read_in[i].replace("\n",""))
    dna = "".join(dna_concat)
    new_entry = FastaInstance(name, dna)
    fasta_list.append(new_entry)

    return(fasta_list)
        
