import subprocess,os,sys,time
import random
from datetime import timedelta
# import keyboard

## python start_script.py a2a8918ca85bafe22016d0bc6bc39797
## conda activate && python start_script.py a2a8918ca85bafe22016d0bc6bc39798
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
p = 115792089237316195423570985008687907852837564279074904382605163141518161494337 + 432420386565659656852420866390673177326
intial_increment_val = sys.argv[1]
if intial_increment_val is not None:
    increment_val = intial_increment_val.upper()
else:
    print("Script needs Argument!!")
    sys.exit(1)

project_folder = os.path.dirname(os.path.realpath(__file__))
print(project_folder)    


range_val = 46

for num in range(60):
    start_time = time.monotonic()
    print(f"Program executed with argument: {increment_val}")
    out_filename = f"240_{increment_val}_{range_val}.txt"

    command = f"./vanitysearch -gpuId 0 -start {increment_val} -range {range_val} -o {out_filename}"
    process = subprocess.Popen(command, shell=True, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
    output,error = process.communicate()
    print(output.decode())
    print(error.decode())
    print(process.returncode)
    process.wait()
    print(process.returncode)

    #if process.returncode != 0 or process.returncode != 3221226356:
    if process.returncode != 0:
        print("Error Running Subprocess")
        break

    print(f"Subprocess completed with argument: {increment_val}")
    end_time = time.monotonic()

    print(f"Time Taken: {timedelta(seconds=end_time-start_time)} !!")


    time.sleep(100)
    print(f"100 Seconds sleep time completed!!")

    #increment_val = (int(increment_val,16) + 2**42-1)%n
    increment_val = (int(increment_val,16) + random.randint(2**121,2**122) -1)%n
    increment_val = hex(increment_val)[2:].upper()
    # if keyboard.is_pressed('q'):
    #     break

print("Program start_gen stopped!!")




