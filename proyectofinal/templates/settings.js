let cantidad = 0;

function modificarCantidad(id, unidades) {
    const cantidadIngresada = document.getElementById(id)
    cantidad += unidades;
    if (cantidad <= 0) {
        cantidad = 0;
    }
    cantidadIngresada.value = cantidad;
}