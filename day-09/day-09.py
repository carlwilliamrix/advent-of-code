from collections import defaultdict

with open("input.txt") as f:
    data = f.read().strip()
data = list(map(int, data))

test = "2333133121414131402"
data = list(map(int, test))

def write_disk(raw_data):
    disk = []
    for i, x in enumerate(raw_data):
        disk += [None if i % 2 else i // 2] * x
    return disk

def compact_disk(disk, head):
    while head < len(disk):
        if disk[head]:
            head += 1
        elif disk:
            cur = disk.pop()
            disk[head] = cur
        #elif cur := disk.pop():
        #    disk[head] = cur
    return disk

def checksum(disk):
    total = 0

    for i, num in enumerate(disk):
        total += i * num
    return total

def part_two(raw_data):
    # Trying a different approach
    unsorted_disk = []

    cur = True
    index = 0
    for i, n in enumerate(raw_data):
        if cur:
            unsorted_disk.append((index, n))
            cur = False
            index += 1
        else:
            if n != 0:
                unsorted_disk.append((None, n))
            cur = True

    print(f"files: {unsorted_disk}")

    additional_index = 0
    sorted_disk = unsorted_disk.copy()

    #for i, file in enumerate(reversed(unsorted_disk)):
    for i, file in zip(range(len(unsorted_disk) - 1, -1, -1), reversed(unsorted_disk)):
        print(f"file first {file}")
        for j, space in enumerate(sorted_disk):
            if file[0] is None:
                break
            else:
                print(f"space first {space}")
                if file[1] > space[1] and space[0] is not None:
                    continue
                else:
                    if file[1] <= space[1] and space[0] is None:
                        print(f"item {file}")
                        sorted_disk[j] = file
                        sorted_disk[i] = (None, file[1])
                        space_left = space[1] - file[1]

                        if 0 < int(space_left):
                            print(f"before adding None  {sorted_disk}")
                            sorted_disk.insert(j + 1, (None, space_left))
                            additional_index += 1
                            print(f"after adding None  {sorted_disk}")

                        sorted_disk[i+1 + additional_index] = (None, file[1])
                        print(f" for sorted j  {j}: {sorted_disk}")
                        #print(f" for unsorted i {i}: {unsorted_disk}")

                        # Compact None tuples
                        t = 0
                        while t < len(sorted_disk) - 1:
                            if sorted_disk[t][0] is None and sorted_disk[t + 1][0] is None:
                                # Combine the tuples
                                sorted_disk[t] = (None, sorted_disk[t][1] + sorted_disk[t + 1][1])
                                # Remove the next tuple
                                #sorted_disk.pop(t + 1)
                                del sorted_disk[t]
                                additional_index -= 1
                            else:
                                t += 1
                        print(f"after sort t {sorted_disk}")
                        break
    return sorted_disk

def checksum_with_null(disk):
    checksum = 0
    position = 1

    for file_id, size in disk:
        if file_id is not None:  # Skip empty spaces
            checksum += sum(position + i for i in range(size)) * file_id
        position += size

    return checksum


print(data)
d = part_two(data)
print(d)
print(checksum_with_null(d))
#print(checksum_with_null(part_two(data)))
#print(part_two(data))
#6349492251099
#18946245938652
#2858


#re = compact_disk(write_disk(data), data[0])
#print(f"The checksum is {checksum(re)}")
# 6334655979668