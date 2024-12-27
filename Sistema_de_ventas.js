// lo primero que hacemos es crear una clase producto con un constructor que recibe dos parametros nombre y precio
class Producto {
    // creamos un contador de productos que inicia en 0
    static contadorProductos = 0;
    constructor(nombre, precio) {
        // creamos un id para cada producto que se incremente en 1
        this._idProducto = ++Producto.contadorProductos;
        // asignamos el nombre y el precio a cada producto
        this._nombre = nombre;
        this._precio = precio;
    }// creamos los metodos get y set para cada atributo
    get idProducto() {
        return this._idProducto;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        return this._nombre = nombre;
    }
    get precio() {
        return this._precio;
    }
    set precio(precio) {
        return this._precio = precio;
    }// creamos un metodo toString para mostrar los atributos de cada producto
    toString() {
        return this.idProducto + " " + this.nombre + " " + this.precio;
    }
}
// creamos una clase orden con un contador de ordenes que inicia en 0
class Orden {
    static contadorOrdenes = 0;
    // creamos un atributo productos que es un arreglo
    static get MAX_PRODUCTOS() {
        return 5;
    }// creamos un constructor que inicializa el id de la orden y el arreglo de productos
    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this.productosAgregados = 0;
    }
    get idOrden() {
        return this._idOrden;
    }// creamos un metodo para agregar productos a la orden
    agregarProductos(producto) {
        if (this._productos.length < Orden.MAX_PRODUCTOS) {
            this._productos.push(producto);
        }
        else {
            return console.log("no se pueden agregar mas productos");
        }
    }// creamos un metodo para calcular el total de la orden
    calcularTotal() {
        let totalVenta = 0;
        for (let producto of this._productos) {
            totalVenta += producto.precio;
        }
        return totalVenta;
    }// creamos un metodo para mostrar la orden
    mostrarOrden() {
        let productosOrden = " ";
        for (let producto of this._productos) {
            productosOrden += producto.toString() + " ";
        }
        console.log(`Orden: ${this._idOrden} Total: ${this.calcularTotal()} Productos: ${productosOrden}`);
    }
}
// creamos un objeto producto y un objeto orden
let producto1 = new Producto("casco", 200);
let producto2 = new Producto("jean", 150);
let orden1 = new Orden();
// agregamos productos a la orden y mostramos la orden
orden1.agregarProductos(producto1);
orden1.agregarProductos(producto2);
orden1.mostrarOrden();