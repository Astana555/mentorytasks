from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256
from datetime import datetime, timedelta, timezone  # Добавлен импорт timezone

# Генерация закрытого ключа
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Создание самоподписанного сертификата
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u'localhost')
])

now = datetime.now(timezone.utc)  # Получение текущего времени с таймзоной

cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    now
).not_valid_after(
    now + timedelta(days=365)
).sign(private_key, SHA256(), default_backend())

# Сохранение сертификата и закрытого ключа в файлы
with open("server.crt", "wb") as cert_file:
    cert_file.write(cert.public_bytes(serialization.Encoding.PEM))

with open("server.key", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))
