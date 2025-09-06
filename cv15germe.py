while True:
    cv2.setMouseCallback("Orjinal Goruntu",tiklamaAl)
    bukmeSekli = cv2.getPerspectiveTransform(baslangic,yeniyer)
    bukulmusSekli = cv2.warpPerspective(goruntu1, bukmeSekli, (sutun,satir))


    cv2.imshow("Bukulmus sekli", bukulmusSekli)
    if cv2.waitKey(1) == ord("q") : break
# cv2.waitKey(0)


cv2.destroyAllWindows()
