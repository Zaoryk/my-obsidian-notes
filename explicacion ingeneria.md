# Sistema de Gestión Empresarial

## Documentación de Componentes

---

## Módulo de Gestión de Inventario

### 1. Gestión de Productos

**Propósito:** Administrar el catálogo completo de productos de la empresa.

**Funcionalidades:**

- Crear y registrar nuevos productos con información detallada
- Actualizar datos de productos existentes (nombre, lote, precio)
- Gestionar fechas de vencimiento para control de caducidad
- Monitorear niveles de stock en tiempo real
- Asignar y controlar lotes de productos para trazabilidad
- Consultar historial de productos

**Conexiones:**

- **Base de datos:** Tabla `producto`
- **Relacionado con:** Gestión de Costos, Control de Movimientos, Órdenes de Producción

---

### 2. Gestión de Bodegas

**Propósito:** Administrar las ubicaciones físicas de almacenamiento.

**Funcionalidades:**

- Crear y configurar bodegas/almacenes
- Definir ubicaciones específicas dentro de cada bodega
- Asignar capacidades y características a cada bodega
- Controlar qué productos se almacenan en cada ubicación
- Generar reportes de ocupación por bodega

**Conexiones:**

- **Base de datos:** Tabla `bodega`
- **Relacionado con:** Control de Movimientos

---

### 3. Control de Movimientos

**Propósito:** Registrar y controlar todas las transacciones de inventario.

**Funcionalidades:**

- Registrar entradas de productos (compras, devoluciones, producción)
- Registrar salidas de productos (ventas, mermas, consumo)
- Transferencias entre bodegas
- Validar que las salidas no excedan el stock disponible
- Mantener trazabilidad completa de movimientos
- Generar reportes de movimientos por período

**Validaciones críticas:**

- Control de stock: No permite salidas mayores al inventario disponible
- Tipos de movimiento: Entrada/Salida/Transferencia
- Trazabilidad: Fecha, cantidad, bodega origen/destino

**Conexiones:**

- **Base de datos:** Tabla `movimientoinventario`
- **Recibe datos de:** Órdenes de Producción (genera movimientos automáticos)
- **Relacionado con:** Productos, Bodegas

---

### 4. Gestión de Costos

**Propósito:** Controlar y analizar los costos asociados a cada producto.

**Funcionalidades:**

- Registrar diferentes tipos de costos (producción, almacenamiento, transporte)
- Asociar costos específicos a productos
- Calcular costos totales por producto
- Analizar evolución de costos en el tiempo
- Generar reportes de rentabilidad

**Conexiones:**

- **Base de datos:** Tabla `costo`
- **Relacionado con:** Productos

---

## Módulo de Compras

### 5. Gestión de Proveedores

**Propósito:** Administrar la base de datos de proveedores.

**Funcionalidades:**

- Registrar nuevos proveedores con información completa
- Mantener datos de contacto actualizados (teléfono, email, dirección)
- Evaluar desempeño de proveedores
- Consultar historial de compras por proveedor
- Gestionar contratos y condiciones comerciales

**Conexiones:**

- **Base de datos:** Tabla `proveedor`
- **Relacionado con:** Órdenes de Compra

---

### 6. Órdenes de Compra

**Propósito:** Gestionar el proceso completo de adquisición de productos.

**Funcionalidades:**

- Crear órdenes de compra a proveedores
- Especificar productos, cantidades y precios
- Gestionar estados del ciclo de vida de la orden
- Calcular montos totales automáticamente
- Hacer seguimiento de entregas
- Generar reportes de compras

**Estados del proceso:**

- **No iniciado:** Orden creada pero no enviada al proveedor
- **En proceso:** Orden enviada, esperando recepción
- **Cerrada:** Orden completada y recibida

**Impacto en otros módulos:**

- Al completarse, actualiza el inventario de productos
- Puede generar órdenes desde el módulo de ventas (pedidos)

**Conexiones:**

- **Base de datos:** Tabla `ordendecompra`
- **Relacionado con:** Proveedores, Gestión de Productos
- **Genera:** Movimientos de inventario (entradas)

---

## Módulo de Producción

### 7. Planificación

**Propósito:** Planificar y programar la producción de productos.

**Funcionalidades:**

- Analizar demanda y capacidad productiva
- Crear planes de producción basados en pedidos
- Optimizar recursos y tiempos de producción
- Programar órdenes de producción
- Generar reportes de planificación

**Conexiones:**

- **Relacionado con:** Órdenes de Producción

---

### 8. Órdenes de Producción

**Propósito:** Ejecutar y controlar el proceso productivo.

**Funcionalidades:**

- Crear órdenes de producción para fabricar productos
- Asignar usuarios responsables de la producción
- Definir fechas de inicio y fin de producción
- Controlar estados de producción (pendiente, en proceso, completada)
- Registrar cantidades producidas
- Consumir materias primas del inventario

**Impacto en otros módulos:**

- Genera movimientos de inventario automáticamente
- Al completarse, actualiza stock de productos terminados
- Registra consumo de materias primas

**Conexiones:**

- **Base de datos:** Tabla `ordenproduccion`
- **Relacionado con:** Productos, Usuarios, Control de Movimientos
- **Genera:** Movimientos de inventario (salidas de MP, entradas de PT)

---

## Módulo de Ventas

### 9. Gestión de Clientes

**Propósito:** Administrar la cartera de clientes de la empresa.

**Funcionalidades:**

- Registrar nuevos clientes con datos completos
- Clasificar clientes por tipo (minorista, mayorista, corporativo)
- Mantener historial de transacciones por cliente
- Gestionar condiciones comerciales específicas
- Analizar comportamiento de compra

**Conexiones:**

- **Base de datos:** Tabla `cliente`
- **Relacionado con:** Gestión de Pedidos, Lista de Precios

---

### 10. Gestión de Pedidos

**Propósito:** Procesar y gestionar los pedidos de clientes.

**Funcionalidades:**

- Crear pedidos de clientes con productos y cantidades
- Calcular montos totales considerando precios y descuentos
- Asignar usuarios responsables del pedido
- Vincular pedidos con órdenes de compra cuando sea necesario
- Hacer seguimiento del estado del pedido
- Generar documentos de venta

**Impacto en otros módulos:**

- Puede generar órdenes de compra si no hay stock suficiente
- Reduce stock de productos al confirmar el pedido

**Conexiones:**

- **Base de datos:** Tabla `pedido`
- **Relacionado con:** Clientes, Usuarios, Órdenes de Compra
- **Genera:** Órdenes de compra cuando se requiere

---

### 11. Lista de Precios

**Propósito:** Gestionar precios diferenciados por canal y temporada.

**Funcionalidades:**

- Definir precios por canal de venta (online, tienda, mayorista)
- Configurar precios por temporada (alta, baja, especial)
- Asignar listas de precios específicas a clientes
- Actualizar precios masivamente
- Consultar historial de cambios de precios

**Conexiones:**

- **Base de datos:** Tabla `listarprecios`
- **Relacionado con:** Clientes

---

## Módulo de Administración

### 12. Gestión de Usuarios

**Propósito:** Administrar los usuarios del sistema.

**Funcionalidades:**

- Crear y configurar cuentas de usuario
- Asignar roles y permisos
- Gestionar credenciales de acceso
- Mantener información de contacto
- Auditar actividades de usuarios

**Roles disponibles en el sistema:**

1. **Administrador:** Acceso completo al sistema
2. **Operador de Compras:** Gestiona proveedores y órdenes de compra
3. **Operador de Inventario:** Controla movimientos y stock
4. **Operador de Producción:** Gestiona órdenes de producción
5. **Operador de Ventas:** Gestiona clientes y pedidos
6. **Analista Financiero:** Acceso a reportes financieros y costos

**Conexiones:**

- **Base de datos:** Tabla `usuario`
- **Relacionado con:** Todos los módulos operacionales

---

### 13. Control de Acceso

**Propósito:** Gestionar la seguridad y permisos del sistema.

**Funcionalidades:**

- Autenticar usuarios en el sistema
- Autorizar acceso a funcionalidades según rol
- Registrar intentos de acceso
- Gestionar sesiones de usuario
- Aplicar políticas de seguridad

**Conexiones:**

- **Relacionado con:** Gestión de Usuarios

---

## Capa de Datos

### Base de Datos

La base de datos está organizada en tres categorías:

#### **Tablas Core** (Entidades fundamentales)

- `producto`: Información de productos
- `bodega`: Almacenes y ubicaciones
- `cliente`: Base de clientes
- `proveedor`: Base de proveedores
- `usuario`: Usuarios del sistema

#### **Tablas Operacionales** (Transacciones y procesos)

- `movimientoinventario`: Registro de entradas/salidas
- `ordendecompra`: Órdenes a proveedores
- `ordenproduccion`: Órdenes de fabricación
- `pedido`: Pedidos de clientes

#### **Tablas Financieras** (Información económica)

- `costo`: Costos asociados a productos
- `listarprecios`: Precios por canal y temporada

---

## Flujos de Integración entre Módulos

### Flujo 1: Proceso de Compra → Inventario

1. Se crea una **Orden de Compra** en el módulo de compras
2. Al cambiar estado a "Cerrada", se genera automáticamente un **Movimiento de Inventario** (entrada)
3. El **stock del producto** se actualiza en la Gestión de Productos

### Flujo 2: Proceso de Producción → Inventario

1. Se crea una **Orden de Producción**
2. Durante la producción, se registran **Movimientos de Inventario**:
    - Salidas: Consumo de materias primas
    - Entradas: Productos terminados
3. El inventario se actualiza en tiempo real

### Flujo 3: Proceso de Venta → Compra

1. Se recibe un **Pedido** de cliente en Gestión de Pedidos
2. Si no hay stock suficiente, se genera automáticamente una **Orden de Compra**
3. La orden de compra, al completarse, actualiza el inventario
4. El pedido puede ser satisfecho

---

## Características Especiales del Sistema

### Trazabilidad

- Cada producto tiene un lote único
- Todos los movimientos quedan registrados con fecha, usuario y bodega
- Se puede rastrear el recorrido completo de cualquier producto

### Validaciones de Negocio

- No se permiten salidas mayores al stock disponible
- Los estados de órdenes siguen un flujo controlado
- Las fechas de vencimiento alertan sobre productos próximos a caducar

### Control de Acceso por Roles

- Cada usuario solo puede acceder a las funcionalidades de su rol
- Separación de responsabilidades para mayor seguridad
- Auditoría de todas las operaciones realizadas

---

## Conclusión

Este sistema integra cinco módulos principales que trabajan de forma coordinada:

- **Inventario** controla los productos y su ubicación
- **Compras** gestiona proveedores y adquisiciones
- **Producción** planifica y ejecuta la fabricación
- **Ventas** atiende a clientes y pedidos
- **Administración** controla usuarios y accesos

Todos los módulos se conectan a través de una base de datos centralizada que mantiene la integridad y consistencia de la información empresarial.

## TL;DR

Tienes un sistema que controla todo el negocio. Se divide en 5 partes principales:

**Inventario** - Lleva el control de tus productos: qué tienes, dónde está y cuánto cuesta.

**Compras** - Te ayuda a comprar materiales a proveedores cuando necesitas reponer stock.

**Producción** - Transforma tus materiales en productos terminados.

**Ventas** - Gestiona a tus clientes, sus pedidos y los precios.

**Administración** - Controla quién puede usar el sistema y qué puede hacer.

Todo está conectado: cuando vendes algo, se reduce tu inventario; cuando produces, consumes materiales y creas nuevos productos; cuando compras, aumentas tu inventario.

Es como una cadena donde cada parte depende de la otra para que el negocio funcione sin problemas.