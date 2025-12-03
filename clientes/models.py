from django.db import models


class Cliente(models.Model):
    codigo = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    whatsapp = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        # SE O CÓDIGO NÃO EXISTIR, GERA AUTOMATICAMENTE
        if not self.codigo:
            last_codigo = Cliente.objects.filter(codigo__startswith='CLI').order_by('-codigo').first()

            if last_codigo:
                # extrai a parte numérica para incrementar
                num = int(last_codigo.codigo.replace('CLI', ''))
                self.codigo = f"CLI{num + 1:04d}"  # CLI0001, CLI0002…
            else:
                self.codigo = "CLI0001"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"