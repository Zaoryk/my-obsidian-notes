## REQUERIMIENTO DESARROLLO - PROYECTO DULCERÍA LILIS

### Objetivo del Documento
- [x] Visión técnica inicial de módulos Maestros y Transaccionales
- [x] Definir campos y atributos para entidades principales
- [x] Mockups de interfaz como referencia visual (modo claro)
- [x] Insumo base para análisis y diseño en Django o similar

---

## Módulos del Sistema

### 1. Módulo de Autenticación / Login
**No es maestro, pero define formularios clave**

#### Formularios:
- [x] **Iniciar sesión**
  - [x] usuario_o_email (requerido)
  - [x] password (requerido, no se almacena en vistas)
  - [x] recordarme (opcional)

- [x] **Olvidé mi contraseña**
  - [x] email (requerido, debe existir)

- [x] **Restablecer contraseña (con token)**
  - [x] token (requerido, solo lectura en UI)
  - [x] nueva_password (requerida, ≥12 caracteres, complejidad)
  - [x] confirmar_password (requerida, debe coincidir)

- [x] **Cambiar contraseña (usuario autenticado)**
  - [x] password_actual (requerida)
  - [x] nueva_password
  - [x] confirmar_password

- [ ] **MFA (opcional)**
  - [ ] codigo_totp (requerido cuando MFA activo)

---

### 2. Módulo Usuarios (Maestro)
**Administra información de usuarios del sistema**

#### Campos:
- [x] **Identificación**
  - [x] username (requerido, único)
  - [x] email (requerido, único)
  - [x] nombres (requerido)
  - [x] apellidos (requerido)

- [x] **Estado y acceso**
  - [x] rol (requerido)
  - [x] estado (requerido; default: ACTIVO)
  - [x] mfa_habilitado (requerido; default: 0)
  - [x] ultimo_acceso (solo lectura)
  - [x] sesiones_activas (contador/solo lectura)

- [x] **Metadatos**
  - [x] area/unidad (opcional)
  - [x] observaciones (opcional)

#### Funcionalidades:
- [x] CRUD completo de usuarios
- [x] Gestión de roles y permisos
- [x] Control de estado (activo, bloqueado, desactivado)
- [x] Historial de accesos y auditoría

---

### 3. Módulo Productos (Maestro)
**Centraliza la gestión de productos**

#### Campos:
- [x] **Identificación**
  - [ ] sku (requerido, único)
  - [ ] ean_upc (opcional, único si se usa)
  - [x] nombre (requerido)
  - [x] descripcion (opcional)
  - [x] categoria (requerido)
  - [ ] marca (opcional)
  - [ ] modelo (opcional)

- [x] **Unidades y precios**
  - [x] uom_compra (requerido; ej. UN, CAJA, KG)
  - [x] uom_venta (requerido)
  - [x] factor_conversion (requerido; default: 1)
  - [ ] costo_estandar (opcional)
  - [x] costo_promedio (solo lectura)
  - [ ] precio_venta (opcional)
  - [x] impuesto_iva (requerido; ej. 19%)

- [x] **Stock y control**
  - [x] stock_minimo (requerido; default: 0)
  - [ ] stock_maximo (opcional)
  - [ ] punto_reorden (opcional; si no, usar mínimo)
  - [x] perishable (requerido; default: 0)
  - [x] control_por_lote (requerido; default: 0)
  - [x] control_por_serie (requerido; default: 0)

- [x] **Relaciones y soporte**
  - [x] imagen_url (opcional)
  - [ ] ficha_tecnica_url (opcional)

- [x] **Derivados (solo lectura)**
  - [x] stock_actual (calculado)
  - [x] alerta_bajo_stock (calculado)
  - [x] alerta_por_vencer (si perishable/lote)

---

### 4. Módulo Proveedores (Maestro)
**Gestiona información de proveedores**

#### Campos:
- [x] **Identificación legal y contacto**
  - [x] rut_nif (requerido, único)
  - [x] razon_social (requerido)
  - [x] nombre_fantasia (opcional)
  - [x] email (requerido)

- [x] **Dirección**
  - [x] pais (requerido; default: "Chile")

- [x] **Comercial**
  - [x] condiciones_pago (requerido)
  - [x] moneda (requerido; ej. CLP)
  - [x] estado (requerido; ENUM: ACTIVO, BLOQUEADO)

- [x] **Relación con productos (vista asociada)**
  - [x] producto_id (FK, requerido al asociar)
  - [x] costo (requerido)
  - [x] lead_time_dias (requerido; default: 7)
  - [ ] min_lote (opcional; default: 1)
  - [x] descuento_ptt (opcional)
  - [x] preferente (requerido; default: 0)

#### Validaciones:
- [x] rut_nif único
- [x] email válido
- [x] Al marcar preferente: una por producto (o permitir varias pero destacar una)

---

### 5. Módulo Transaccional (Inventario)
**Gestiona movimientos de inventario y trazabilidad**

#### Características:
- [x] **Tipos de movimiento**: ingresos, salidas, ajustes, devoluciones, transferencias
- [x] **Datos del movimiento**: fecha, tipo, producto, proveedor, bodega, cantidad
- [x] **Control avanzado**: manejo por lotes, series y fechas de vencimiento

#### Campos en formulario de movimiento:
- [x] doc_referencia
- [x] motivo (para ajustes/devoluciones)
- [x] observaciones
- [x] Campos específicos por tipo de movimiento

---

## Mockups de Referencia
**Nota**: Los diseños son solo referenciales para guiar el desarrollo

### Interfaces incluidas:
- [x] Login y recuperación de contraseña
- [x] Formulario de usuarios con tabla de datos
- [x] Formulario de productos con pestañas:
  - [x] 1. Identificación y precios
  - [x] 2. Stock y control
  - [x] 3. Relaciones y derivados
- [x] Formulario de proveedores con pestañas:
  - [x] 1. Identificación y contacto
  - [x] 2. Dirección y comercial
  - [x] 3. Relación con productos
- [x] Módulo de inventario con registro de movimientos

---

## Consideraciones Técnicas
- [x] Los mockups están en modo claro (solo referencia visual)
- [x] Desarrollo posterior en Django o frameworks similares
- [x] Asegurar consistencia de datos y escalabilidad
- [x] Implementar validaciones de datos y negocios
- [x] Considerar auditoría y trazabilidad en transacciones

---

## Próximos Pasos
- [x] Validar requerimientos con stakeholders
- [x] Definir modelo de datos detallado
- [x] Establecer arquitectura técnica
- [x] Planificar sprints de desarrollo
- [x] Implementar módulos prioritarios primero
- [ ] Realizar pruebas y ajustes