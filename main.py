class A:
    def __init__(self, idx: int):
        self.idx = idx


    def __getitem__(self, item):
        return self.idx


    def __len__(self):
        return 2


if __name__ == '__main__':
    a = A(4)
    print(a[0])
    print(a[1])
