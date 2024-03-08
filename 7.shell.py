import subprocess

while True:
    command = input("$ ")
    if ">" in command:
        cmd, output_file = command.split(">")
        with open(output_file.strip(), 'w') as f:
            subprocess.run(cmd.strip().split(), stdout=f)
    elif "<" in command:
        cmd, input_file = command.split("<")
        with open(input_file.strip(), 'r') as f:
            subprocess.run(cmd.strip().split(), stdin=f)
    elif "|" in command:
        cmd1, cmd2 = command.split("|")
        p1 = subprocess.Popen(cmd1.strip().split(), stdout=subprocess.PIPE)
        p2 = subprocess.Popen(cmd2.strip().split(), stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        output = p2.communicate()[0]
        print(output.decode())
    else:
        subprocess.run(command.split())