from bs4 import BeautifulSoup
from descarga import Descarga
from guardar import Guardar

class Scraping():
    def __init__(self, link:str):
        self.link = link
        self.html = BeautifulSoup(Descarga().descargar(self.link), 'html.parser')
        self._categorias = {}
        self._libros = {}
        self._informacion_libros = []
        
    def buscar_categorias(self) -> None:
        """Busca las categorias de la pagina web"""
        print(f"Connect: {self.link}")
        print("Getting data...")
        categorias = self.html.find('ul', class_='nav nav-list').find_all('li')
        for categoria in categorias:
            categoria_key = f'{categoria.find('a').text.strip()}'
            categoria_link = f'{self.link}/{categoria.find("a").get("href")}'
            print(f"Extracting: Categoria({categoria_key}), link({categoria_link})")
            self._categorias[categoria_key] = categoria_link
        del self._categorias['Books']

    def buscar_libros(self):
        """Busca los libros de la pagina web"""
        for _, (categoria, link) in enumerate(self._categorias.items()):
            full_link = link

            print(f"Connect: {full_link}")
            html = BeautifulSoup(Descarga().descargar(full_link), 'html.parser')
            
            print(f"Getting data...")
            # Busca los libros en el index de cada categoria
            libros = html.find('ol', class_='row').find_all('li')

            tmp_libros = []
            for libro in libros:
                data = f'{self.link}/catalogue{libro.find("a")["href"].split('/..')[-1]}'
                print(f"Extracting: {data}")
                tmp_libros.append({
                    'link': data,
                    })
            self._libros[categoria] = tmp_libros

            tiene_indice = html.find('div', class_='col-sm-8 col-md-9').find('li', class_='current')
            # tiene_indice = html.find('li', class_='current')
            if tiene_indice:
                print(f"Have index...")
                indice = tiene_indice.text.split()[-1]
                print(f"Getting index from {categoria}...")
                for i in range(1, int(indice) + 1):
                    full_link = f'{full_link}?page={i}.html'
                    print(f"Connect: {full_link}")
                    html = BeautifulSoup(Descarga().descargar(full_link), 'html.parser')
        
                    # Busca los libros en el index de cada categoria
                    libros = html.find('ol', class_='row').find_all('li')
                    print("Getting data...")
                    tmp_libros = []
                    for libro in libros:
                        data = f'{self.link}/catalogue{libro.find("a")["href"].split('/..')[-1]}'
                        print(f"Extracting: {data}")
                        tmp_libros.append({
                            'link': data,
                            })
                    self._libros[categoria] = tmp_libros

    def buscar_libro_individual(self):
        """Busca los libros de la pagina web"""
        pass

    def buscar_libros_del_link(self):
        """Busca los libros de la pagina web"""
        for categoria, links in self._libros.items():
            # print(categoria, link)
            for link in links:
                link = link['link']
                print(f"Connect: {categoria} {link}")
                html = BeautifulSoup(Descarga().descargar(link), 'html.parser')

                print("Extracting information...")
                title = html.find('article', class_='product_page').find('h1').text.strip()
                precio = html.find('p', class_='price_color').text.strip()
                en_stock = html.find('p', class_='instock').find('i', class_='icon-ok').text.strip()
                rating = html.find('p', class_='star-rating').attrs['class'][1]
                imagen_link = self.link + '/' + html.find('div', class_='item').find('img').attrs['src'].split('../')[-1]
                existe_etiqueta_descripcion = html.find('div', id='product_description')
                if existe_etiqueta_descripcion and existe_etiqueta_descripcion.next_sibling:
                    descripcion = html.find('div', id='product_description').find_next_sibling('p').text
                else:
                    descripcion = None

                print(f"Data: {categoria}, {title}, {precio}, {en_stock}, {rating}, {imagen_link}, {descripcion}")

                self._informacion_libros.append({
                    'categoria': categoria,
                    'titulo': title,
                    'precio': precio,
                    'en_stock': en_stock,
                    'rating': rating,
                    'imagen': imagen_link,
                    'descripcion': descripcion,
                })
                print(self._informacion_libros)

    def run(self):
        self.buscar_categorias()
        Guardar().categorias_como_csv('categorias', self._categorias)
        self.buscar_libros()
        Guardar().libros_como_csv('libros', self._libros)
        self.buscar_libros_del_link()
        Guardar().libros_como_csv('libros', self._informacion_libros)


if __name__=='__main__':

    link = 'https://books.toscrape.com'

    scraping = Scraping(link)
    scraping.run()


    # links = ['https://books.toscrape.com/catalogue/delivering-the-truth-quaker-midwife-mystery-1_464/index.html',
    # 'https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html']
    # scraping.buscar_libros_del_link()
    