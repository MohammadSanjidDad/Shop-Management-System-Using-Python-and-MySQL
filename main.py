from core.root import MainClass

# todo: press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = MainClass(database_password='@MohammadSanjidDad01637965108', database_name='ShopDB')
    test.show_database_tables('ShopDB', 'PRODUCTS')
