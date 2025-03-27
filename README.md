# DemiGod Phoenix 2.0
## Descripción
Sistema multiagente de IA para generar ingresos pasivos mediante una red micelial autoorganizada, con una matriz de usuarios que genera comisiones del 20%.

## Requisitos
- Ubuntu 22.04 LTS.
- Python 3.10, pip, git.
- AWS EC2 (t3.medium y t3.micro).
- Cuentas en Telegram, Bitly Premium, Namecheap.

## Instalación
1. **Configura AWS**:
   - Regístrate en aws.amazon.com.
   - Lanza t3.medium ("DemiGodPhoenix") y t3.micro ("PhoenixAI-Sub").
   - Conéctate vía SSH y actualiza: `sudo apt update && sudo apt install python3 python3-pip git -y`.
2. **Compra un Dominio**:
   - En Namecheap, compra "demigodphoenix.com" (5.90 EUR).
   - Vincula a la IP de t3.medium con Route 53.
3. **Configura Bitly Premium**:
   - Suscríbete por 7.27 EUR y personaliza enlaces.
4. **Clona y Configura**:
   - `git clone https://github.com/tu-usuario/DemiGodPhoenix.git`.
   - Edita archivos en `core/` e `integrations/` con tus claves/tokens.
5. **Ejecuta**:
   - En t3.medium: `python ui/app.py &` y `python core/system_core.py`.
   - En t3.micro: `python core/system_core_sub.py`.
6. **¡Listo!**:# DemiGodPhoenix
