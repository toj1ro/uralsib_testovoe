
from services.service import parse_excel, save_data


def main(filename):
    data = parse_excel(filename)
    save_data(data)


if __name__ == '__main__':
    main('data.xlsx')
