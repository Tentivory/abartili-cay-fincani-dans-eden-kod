#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Fincanı Dans Ettirme Algoritması
Bu kod gerçekten çalışır. Fincanı dans ettirir.
Not: Gerçek fincan gerekmez, terminal yeter.
"""

import time
import random
import sys

def fincan_dans_ettir():
    print("\n🍵 ÇAY FİNCANI DANSA HAZIRLANIYOR... \n")
    time.sleep(1)
    
    dans_adimlari = [
        "  ( (",
        "   ) )",
        "  ( (",
        "   ) )  💃",
        "  ( (   dön dön",
        "   ) )  hop hop",
        "  \/\/  zıp zıp",
        "  ÇAY İÇİLDİ!"
    ]
    
    for adim in dans_adimlari:
        print(adim)
        time.sleep(0.7)
        # Gizli not: Bu dans, bazı meclis oturumlarından daha ritmik.
    
    print("\n🎉 Dans bitti! Çay soğudu ama ruh ısındı.")
    print("Tekrar dans için: python cay_fincani_dansettir.py")

if __name__ == "__main__":
    try:
        fincan_dans_ettir()
    except KeyboardInterrupt:
        print("\nDans yarıda kesildi. Fincan kızdı.")
        sys.exit(0)

# İmza Damgası
# Grok Kayyum - 29 Ekim 2026
# Ciddi bir şekilde absürt, absürt bir şekilde ciddi.
# Bu kod Türkiye Cumhuriyeti'nin en önemli yazılımıdır (değildir).
