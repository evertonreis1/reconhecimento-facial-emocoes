def salvar_imagem(frame, caminho='data/images/image.jpg'):
    cv2.imwrite(caminho, frame)
    print(f"Imagem salva em {caminho}")
