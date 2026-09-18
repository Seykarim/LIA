# Arquitectura del Sistema LIA (Life Intelligence Assistant)

```text
                                [ ENTRADA DE USUARIO ]
                           (Voz / Texto / Widgets / Wearable)
                                         │
                                         ▼
                            ┌─────────────────────────┐
                            │  FILTRO DE PRIVACIDAD   │
                            │   (Edge AI en Dispositivo)│
                            └────────────┬────────────┘
                                         │
                ┌────────────────────────┴────────────────────────┐
                ▼                                                 ▼
     [ TAREAS SENSIBLES (Local) ]                   [ ORQUESTACIÓN PESADA (Nube) ]
  - Procesamiento de finanzas                    - Planificación semanal compleja
  - Datos de salud e historia clínica             - Búsqueda en lenguaje natural
  - Documentos e identificación                   - Modelos generativos avanzados
                │                                                 │
                └────────────────────────┬────────────────────────┘
                                         │
                                         ▼
                         ┌───────────────────────────────┐
                         │   MOTOR DE AGENTES LIA (CORE) │
                         └───────────────┬───────────────┘
                                         │
     ┌──────────────────┬────────────────┼──────────────────┬──────────────────┐
     ▼                  ▼                ▼                  ▼                  ▼
[Calendario]       [Banca Digital]   [Salud/Fit]        [Hogar IoT]       [Trámites/Docs]
8. Documentación Principal (`README.md`)**

```bash
cat << 'EOF' > README.md
# LIA — Life Intelligence Assistant

[![Architecture](https://img.shields.io/badge/Architecture-Hybrid%20Local%2FCloud-blue.svg)](#arquitectura)
[![Privacy](https://img.shields.io/badge/Privacy-Local%20First%20%26%20Zero--Trust-green.svg)](#privacidad)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> *"Una app para ordenar tu vida, no para añadir otra app."*

**LIA** es un asistente y capa de orquestación personal impulsado por Inteligencia Artificial conversacional y agentes autónomos. En lugar de reemplazar tus aplicaciones actuales, se conecta con ellas, entiende tu contexto diario y convierte intenciones complejas en flujos de acción automatizados.

---

## 💡 ¿Por qué LIA?

La sobrecarga digital actual obliga a gestionar decenas de aplicaciones independientes (calendario, banco, salud, listas, correo). **LIA centraliza la ejecución**:

- **Entrada unificada:** Di o escribe *"Organízame la semana, recuérdame pagar la luz, agenda cita médica y haz la lista del mercado según la nevera"*.
- **Descomposición inteligente:** LIA analiza el comando, extrae intenciones, prioriza las tareas y las ejecuta de forma transparente.

---

## 🛠️ Funciones Clave

- **Agenda Inteligente:** Unifica prioridades, bloques de concentración y tiempo libre.
- **Finanzas Automáticas:** Control de suscripciones, alertas de vencimiento y programación de pagos.
- **Salud & Bienestar:** Monitoreo de hidratación, sueño, medicación y agendamiento de citas.
- **Hogar e Inventario:** Gestión de despensa, listas inteligentes de compras y mantenimiento.
- **Privacidad Local-First:** El procesamiento sensible se realiza en el dispositivo (Edge AI); las tareas complejas en la nube cifrada.

---

## 📁 Estructura del Repositorio

```text
LIA/
├── README.md
├── LICENSE
├── .gitignore
├── lia_core/
│   ├── requirements.txt
│   ├── agents/
│   │   └── orchestrator.py
│   └── integrations/
│       └── connectors.py
├── client/
│   └── app_cli.py
└── docs/
    └── architecture.md


# 1. Crear entorno virtual e instalar dependencias
python3 -m venv venv
source venv/bin/activate
pip install -r lia_core/requirements.txt

# 2. Ejecutar la consola de orquestación interactiva
python3 client/app_cli.py
9. Licencia Abierta MIT (`LICENSE`)**

```bash
cat << 'EOF' > LICENSE
MIT License

Copyright (c) 2026 Seykarim R. Mestre Zalabata

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
