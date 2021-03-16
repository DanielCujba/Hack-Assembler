class ParserModule:
    def __init__(self):
        pass
    def parse_file(self,file_name):
        assembly_file=open(file_name,"r")
        segmented_file=[]
        for line in assembly_file:
            line = line.strip()
            if len(line)>1:
                command=[None,None]
                if "//" in line:
                    continue
                elif "(" in line:
                    command[0]="L"
                    command[1]=line.strip("()")
                elif "@" in line:
                    command[0]="A"
                    command[1]=line.strip("@")
                else:
                    command[0]="C"
                    c_command=[None,None,None]
                    start=0
                    end=len(line)
                    if "=" in line:
                        c_command[0]=line.split("=")[0]
                        start=line.index("=")+1
                    if ";" in line:
                        c_command[2]=line.split(";")[1]
                        end = line.index(";")
                    c_command[1]=line[start:end]
                    command[1]=c_command
                segmented_file.append(command)
        assembly_file.close()
        return segmented_file


