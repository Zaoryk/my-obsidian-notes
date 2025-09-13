## REQUERIMIENTO DESARROLLO - PROYECTO DULCERÍA LILIS

### Objetivo del Documento
- [ ] Visión técnica inicial de módulos Maestros y Transaccionales
- [ ] Definir campos y atributos para entidades principales
- [ ] Mockups de interfaz como referencia visual (modo claro)
- [ ] Insumo base para análisis y diseño en Django o similar

---

## Módulos del Sistema

### 1. Módulo de Autenticación / Login
**No es maestro, pero define formularios clave**

#### Formularios:
- [ ] **Iniciar sesión**
  - [ ] usuario_o_email (requerido)
  - [ ] password (requerido, no se almacena en vistas)
  - [ ] recordarme (opcional)

- [ ] **Olvidé mi contraseña**
  - [ ] email (requerido, debe existir)

- [ ] **Restablecer contraseña (con token)**
  - [ ] token (requerido, solo lectura en UI)
  - [ ] nueva_password (requerida, ≥12 caracteres, complejidad)
  - [ ] confirmar_password (requerida, debe coincidir)

- [ ] **Cambiar contraseña (usuario autenticado)**
  - [ ] password_actual (requerida)
  - [ ] nueva_password
  - [ ] confirmar_password

- [ ] **MFA (opcional)**
  - [ ] codigo_totp (requerido cuando MFA activo)

---

### 2. Módulo Usuarios (Maestro)
**Administra información de usuarios del sistema**

#### Campos:
- [ ] **Identificación**
  - [ ] username (requerido, único)
  - [ ] email (requerido, único)
  - [ ] nombres (requerido)
  - [ ] apellidos (requerido)
  - [ ] telefono (opcional)

- [ ] **Estado y acceso**
  - [ ] rol (requerido)
  - [ ] estado (requerido; default: ACTIVO)
  - [ ] mfa_habilitado (requerido; default: 0)
  - [ ] ultimo_acceso (solo lectura)
  - [ ] sesiones_activas (contador/solo lectura)

- [ ] **Metadatos**
  - [ ] area/unidad (opcional)
  - [ ] observaciones (opcional)

#### Funcionalidades:
- [ ] CRUD completo de usuarios
- [ ] Gestión de roles y permisos
- [ ] Control de estado (activo, bloqueado, desactivado)
- [ ] Historial de accesos y auditoría

---

### 3. Módulo Productos (Maestro)
**Centraliza la gestión de productos**

#### Campos:
- [ ] **Identificación**
  - [ ] sku (requerido, único)
  - [ ] ean_upc (opcional, único si se usa)
  - [ ] nombre (requerido)
  - [ ] descripcion (opcional)
  - [ ] categoria (requerido)
  - [ ] marca (opcional)
  - [ ] modelo (opcional)

- [ ] **Unidades y precios**
  - [ ] uom_compra (requerido; ej. UN, CAJA, KG)
  - [ ] uom_venta (requerido)
  - [ ] factor_conversion (requerido; default: 1)
  - [ ] costo_estandar (opcional)
  - [ ] costo_promedio (solo lectura)
  - [ ] precio_venta (opcional)
  - [ ] impuesto_iva (requerido; ej. 19%)

- [ ] **Stock y control**
  - [ ] stock_minimo (requerido; default: 0)
  - [ ] stock_maximo (opcional)
  - [ ] punto_reorden (opcional; si no, usar mínimo)
  - [ ] perishable (requerido; default: 0)
  - [ ] control_por_lote (requerido; default: 0)
  - [ ] control_por_serie (requerido; default: 0)

- [ ] **Relaciones y soporte**
  - [ ] imagen_url (opcional)
  - [ ] ficha_tecnica_url (opcional)

- [ ] **Derivados (solo lectura)**
  - [ ] stock_actual (calculado)
  - [ ] alerta_bajo_stock (calculado)
  - [ ] alerta_por_vencer (si perishable/lote)

---

### 4. Módulo Proveedores (Maestro)
**Gestiona información de proveedores**

#### Campos:
- [ ] **Identificación legal y contacto**
  - [ ] rut_nif (requerido, único)
  - [ ] razon_social (requerido)
  - [ ] nombre_fantasia (opcional)
  - [ ] email (requerido)
  - [ ] telefono (opcional)
  - [ ] sitio_web (opcional)

- [ ] **Dirección**
  - [ ] direccion (opcional)
  - [ ] ciudad (opcional)
  - [ ] pais (requerido; default: "Chile")

- [ ] **Comercial**
  - [ ] condiciones_pago (requerido)
  - [ ] moneda (requerido; ej. CLP)
  - [ ] contacto_principal_nombre (opcional)
  - [ ] contacto_principal_email (opcional)
  - [ ] contacto_principal_telefono (opcional)
  - [ ] estado (requerido; ENUM: ACTIVO, BLOQUEADO)
  - [ ] observaciones (opcional)

- [ ] **Relación con productos (vista asociada)**
  - [ ] producto_id (FK, requerido al asociar)
  - [ ] costo (requerido)
  - [ ] lead_time_dias (requerido; default: 7)
  - [ ] min_lote (opcional; default: 1)
  - [ ] descuento_ptt (opcional)
  - [ ] preferente (requerido; default: 0)

#### Validaciones:
- [ ] rut_nif único
- [ ] email válido
- [ ] Al marcar preferente: una por producto (o permitir varias pero destacar una)

---

### 5. Módulo Transaccional (Inventario)
**Gestiona movimientos de inventario y trazabilidad**

#### Características:
- [ ] **Tipos de movimiento**: ingresos, salidas, ajustes, devoluciones, transferencias
- [ ] **Datos del movimiento**: fecha, tipo, producto, proveedor, bodega, cantidad
- [ ] **Control avanzado**: manejo por lotes, series y fechas de vencimiento

#### Campos en formulario de movimiento:
- [ ] doc_referencia
- [ ] motivo (para ajustes/devoluciones)
- [ ] observaciones
- [ ] Campos específicos por tipo de movimiento

---

## Mockups de Referencia
**Nota**: Los diseños son solo referenciales para guiar el desarrollo

### Interfaces incluidas:
- [ ] Login y recuperación de contraseña
- [ ] Formulario de usuarios con tabla de datos
- [ ] Formulario de productos con pestañas:
  - [ ] 1. Identificación y precios
  - [ ] 2. Stock y control
  - [ ] 3. Relaciones y derivados
- [ ] Formulario de proveedores con pestañas:
  - [ ] 1. Identificación y contacto
  - [ ] 2. Dirección y comercial
  - [ ] 3. Relación con productos
- [ ] Módulo de inventario con registro de movimientos

---

## Consideraciones Técnicas
- [ ] Los mockups están en modo claro (solo referencia visual)
- [ ] Desarrollo posterior en Django o frameworks similares
- [ ] Asegurar consistencia de datos y escalabilidad
- [ ] Implementar validaciones de datos y negocios
- [ ] Considerar auditoría y trazabilidad en transacciones

---

## Próximos Pasos
- [ ] Validar requerimientos con stakeholders
- [ ] Definir modelo de datos detallado
- [ ] Establecer arquitectura técnica
- [ ] Planificar sprints de desarrollo
- [ ] Implementar módulos prioritarios primero
- [ ] Realizar pruebas y ajustes