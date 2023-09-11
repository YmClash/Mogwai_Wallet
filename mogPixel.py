from PIL import Image

class PixelArt:

    def pixel(self, pixelSize, image):
        imageWeidth, imageHeight = image.size

        if pixelSize == "small":
            SIZE =10
        elif pixelSize == "medium":
            SIZE =20
        elif pixelSize == "large":
            SIZE=25
        else:
            return f'MogFaill'

        for y in range(0,imageWeidth,SIZE):
            for x in range(0,imageHeight,SIZE):
                pixel = image.getpixel((x,y))

                for a in range(y,min(y+SIZE,imageWeidth)):
                    for b in range(x,min(x+SIZE,imageHeight)):
                        image.putpixel((b,a),pixel)


        output_filename= f'output{pixelSize.capitalize()}.png'
        image.save(output_filename)

        return f'Image {output_filename} crée avec succès'



img = Image.open(r'C:\Users\y_mc\PycharmProjects\Mogwai_Wallet\Mogwai .PNG')

MogPix = PixelArt()

output =MogPix.pixel("large",img)

