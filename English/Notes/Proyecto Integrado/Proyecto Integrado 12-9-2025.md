## DEVELOPMENT REQUIREMENT - DULCERÍA LILIS PROJECT

### Objective of the Document
- [x] Initial technical overview of Master and Transactional modules
- [x] Define fields and attributes for main entities
- [x] Interface mockups for visual reference (light mode)
- [x] Base input for analysis and design in Django or similar

---

## System Modules

### 1. Authentication / Login Module
**Not master, but defines key forms**

#### Forms:
- [x] **Login**
  - [x] user_or_email (required)
  - [x] password (required, not stored in views)
  - [x] remember me (optional)

- [ ] **I forgot my password**
  - [ ] email (required, must exist)

- [ ] **Reset password (with token)**
  - [ ] token (required, read-only in UI)
  - [ ] new_password (required, ≥12 characters, complexity)
  - [ ] confirm_password (required, must match)

- [ ] **Change password (authenticated user)**
  - [ ] current_password (required)
  - [ ] new_password
  - [ ] confirm_password

- [ ] **MFA (optional)**
  - [ ] totp_code (required when MFA active)

---

### 2. Users Module (Master)
**Manages system user information**

#### Fields:
- [x] **Identification**
  - [x] username (required, unique)
  - [x] email (required, unique)
  - [x] names (required)
  - [x] surnames (required)

- [ ] **Status and access**
  - [ ] role (required)
  - [ ] status (required; default: ACTIVE)
  - [ ] mfa_enabled (required; default: 0)
  - [ ] last_access (read only)
  - [ ] active_sessions (counter/read-only)

- [ ] **Metadata**
  - [ ] area/unit (optional)
  - [ ] observations (optional)

#### Features:
- [ ] Full CRUD of users
- [x] Role and permission management
- [x] Status control (active, locked, disabled)
- [x] Access and audit history

---

### 3. Products Module (Master)
**Centralize product management**

#### Fields:
- [ ] **Identification**
  - [ ] sku (required, unique)
  - [ ] ean_upc (optional, unique if used)
  - [ ] name (required)
  - [ ] description (optional)
  - [ ] category (required)
  - [ ] mark (optional)
  - [ ] model (optional)

- [ ] **Units and prices**
  - [ ] uom_purchase (required; e.g. UN, BOX, KG)
  - [ ] uom_sales (required)
  - [ ] conversion_factor (required; default: 1)
  - [ ] standard_cost (optional)
  - [ ] average_cost (read-only)
  - [ ] sale_price (optional)
  - [ ] vat_tax (required; e.g. 19%)

- [ ] **Stock and control**
  - [ ] minimum_stock (required; default: 0)
  - [ ] maximum_stock (optional)
  - [ ] reorder_point (optional; otherwise use minimum)
  - [ ] perishable (required; default: 0)
  - [ ] batch_control (required; default: 0)
  - [ ] control_per_serial (required; default: 0)

- [ ] **Relationships and support**
  - [ ] image_url (optional)
  - [ ] technical_sheet_url (optional)

- [ ] **Derived (read only)**
  - [ ] current_stock (calculated)
  - [ ] low_stock_alert (calculated)
  - [ ] alert_due_due (if perishable/batch)

---

### 4. Suppliers Module (Master)
**Manage supplier information**

#### Fields:
- [ ] **Legal identification and contact**
  - [ ] rut_nif (required, unique)
  - [ ] company_reason (required)
  - [ ] fantasy_name (optional)
  - [ ] email (required)

- [ ] **Address**
  - [ ] country (required; default: "Chile")

- [ ] **Commercial**
  - [ ] payment_conditions (required)
  - [ ] currency (required; e.g. CLP)
  - [x] status (required; ENUM: ACTIVE, LOCKED)

- [ ] **Relationship with products (associated view)**
  - [x] product_id (FK, required when associating)
  - [x] cost (required)
  - [ ] lead_time_days (required; default: 7)
  - [ ] batch_min (optional; default: 1)
  - [x] ptt_discount (optional)
  - [ ] preferred (required; default: 0)

#### Validations:
- [ ] unique rut_nif
- [ ] valid email
- [ ] When marking preferential: one per product (or allow several but highlight one)

---### 5. Transactional Module (Inventory)
**Manage inventory movements and traceability**

#### Features:
- [ ] **Types of movement**: entries, exits, adjustments, returns, transfers
- [ ] **Movement data**: date, type, product, supplier, warehouse, quantity
- [ ] **Advanced control**: batch management, series and expiration dates

#### Fields in movement form:
- [ ] doc_reference
- [ ] reason (for adjustments/returns)
- [ ] observations
- [ ] Specific fields by type of movement

---

## Reference Mockups
**Note**: The designs are for reference only to guide development

### Interfaces included:
- [ ] Login and password recovery
- [ ] User form with data table
- [ ] Tabbed Product Form:
  - [ ] 1. Identification and prices
  - [ ] 2. Stock and control
  - [ ] 3. Relationships and derivatives
- [ ] Supplier form with tabs:
  - [ ] 1. Identification and contact
  - [ ] 2. Address and commercial
  - [ ] 3. Relationship with products
- [ ] Inventory module with movement registration

---

## Technical Considerations
- [ ] Mockups are in clear mode (visual reference only)
- [ ] Subsequent development in Django or similar frameworks
- [ ] Ensure data consistency and scalability
- [ ] Implement data and business validations
- [ ] Consider auditing and traceability in transactions

---

## Next Steps
- [ ] Validate requirements with stakeholders
- [ ] Define detailed data model
- [ ] Establish technical architecture
- [ ] Plan development sprints
- [ ] Deploy priority modules first
- [ ] Perform tests and adjustments