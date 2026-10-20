from django.db import models

# 1. dirección
class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calle} #{self.numero}, {self.ciudad}"

# 2. categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# 3. proveedor
class Proveedor(models.Model):
    codigo = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    pagina_web = models.URLField()

    def __str__(self):
        return self.nombre

# 4. cliente
class Cliente(models.Model):
    codigo = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# teléfonos del cliente (1 cliente -> N teléfonos)
class TelefonoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='telefonos')
    telefono = models.CharField(max_length=20)

# 5. producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.OneToOneField(Proveedor, on_delete=models.CASCADE)  # 1 a 1 segun indica la actividad

    def __str__(self):
        return self.nombre

# 6. venta (factura)
class Venta(models.Model):
    num_factura = models.CharField(max_length=50, unique=True)
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    monto_final = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Factura {self.num_factura}"

# 7. detalle de la venta (tabla intermedia N:M)
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_momento_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)





