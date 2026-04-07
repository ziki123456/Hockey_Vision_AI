# test_predict.py
# Jednoduchy test bez webu

from predict import load_trained_models, predict_image


def main():
    print("TEST PREDIKCE HOCKEYVISION")
    print("--------------------------")

    image_path = input("Zadej cestu k obrázku: ").strip()

    if not image_path:
        print("Nebyla zadana cesta k obrazku.")
        return

    try:
        binary_model, situation_model = load_trained_models()
        result = predict_image(
            image_path,
            binary_model=binary_model,
            situation_model=situation_model
        )

        print("\nVYSLEDEK")
        print(f"Binarni model: {result['binary_class_name']}")
        print(f"Binarni jistota: {result['binary_confidence'] * 100:.2f} %")
        print(f"Finalni vysledek: {result['final_class_name']}")

        if result["situation_class_name"] is not None:
            print(f"Situace: {result['situation_class_name']}")
            print(f"Jistota situace: {result['situation_confidence'] * 100:.2f} %")
        else:
            print("Situace se neurcovala, protoze obrazek neni hokej.")

    except FileNotFoundError as e:
        print(f"\nChyba modelu: {e}")
    except Exception as e:
        print(f"\nNastala chyba: {e}")


if __name__ == "__main__":
    main()