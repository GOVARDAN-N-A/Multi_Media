import os

class StripingStorage:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.disks = [f'disk{i}' for i in range(1, num_disks + 1)]

        # Create disk directories if they don't exist
        for disk in self.disks:
            os.makedirs(disk, exist_ok=True)

    def write_data(self, file_name, data):
        stripe_size = len(data) // self.num_disks
        for i, disk in enumerate(self.disks):
            start = i * stripe_size
            end = start + stripe_size
            stripe_data = data[start:end]
            file_path = os.path.join(disk, file_name)
            with open(file_path, 'w') as f:
                f.write(stripe_data)

    def read_data(self, file_name):
        data = ''
        for disk in self.disks:
            file_path = os.path.join(disk, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    data += f.read()
        return data

if __name__ == "__main__":
    num_disks = 2  # Change this to the number of disks in your striped setup
    striped_storage = StripingStorage(num_disks)

    # Write data to the striped disks
    data_to_write = "This is striped data storage example using strip-based method."
    striped_storage.write_data("striped_file.txt", data_to_write)

    # Read data from the striped disks
    recovered_data = striped_storage.read_data("striped_file.txt")
    if recovered_data:
        print("Data is available and recovered successfully:")
        print(recovered_data)
    else:
        print("Data cannot be recovered.")
