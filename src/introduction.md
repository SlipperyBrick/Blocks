![Blocks logo](./assets/blocks-logo.png)

# Welcome

```blocks-alert
content: "Blocks is currently in development, with plans to release a public beta for testing soon!"
```

Blocks is a plugin for MDBook which preprocesses "Blocks" markdown into beautiful Bootstrap components.

Elements which are created with Blocks are constructed into Bootstrap components that inherit the default style of your enabled MDBook theme.

Whether you are using MDBook for creating a blogging site, technical documentation, a personal portfolio, or even a complete website solution, Blocks gives you the ability to continue writing your book pages in markdown whilst adding modern looking components straight from the Bootstrap framework.

```blocks-card
title: "Hi!"
caption: "Keep your content looking fresh."
image: "./assets/blocks-watermark.png"
button: "See More"
link: "seemore.md"
align: "True"
```

```blocks-card
title: "Welcome"
caption: "With modern Bootstrap components."
image: "./assets/blocks-watermark.png"
button: "See More"
link: "seemore.md"
align: "True"
```

```blocks-card
title: "To ..."
caption: "That you can write in markdown."
image: "./assets/blocks-watermark.png"
button: "See More"
link: "seemore.md"
align: "True"
```

```blocks-card
title: "Blocks!"
caption: "Using the power of Blocks."
image: "./assets/blocks-watermark.png"
button: "See More"
link: "seemore.md"
align: "True"
```

```blocks-badge
title: "The Basics"
content: "New"
```

Blocks components by default stack down the page. This behaviour can be changed for some selected components *(cards and buttons)* by applying the `align: "True"` attribute.

## Alert

Notify your users when information is important by using an alert. Encapsulate some content within an alert to ensure that critical information is front and center! 

```blocks-alert
content: "Alert! Alert! Alert!"
```

## Button

Buttons are a great way to navigate and redirect your users to other places in your MDBook. Go ahead, press the button and be taken to another page.

```blocks-button
content: "Go Somewhere"
link: "seemore.md"
align: "True"
```

Button components take two attributes, one for their content, and another for their link redirect. Links can be specified by using the paths to your `.md` book files, giving you the freedom to link across pages of your MDBook and also to page headings!

### Alignment

Giving each button component the `align: "True"` attribute encapsulates those components in a row. All buttons within a row are equally spaced and centered on the page. A maximum of four buttons can be placed per row, with automatic wrapping of buttons exceeding the maximum components in a row.

```blocks-button
content: "Go Somewhere"
link: "seemore.md"
align: "True"
```

```blocks-button
content: "Go Somewhere"
link: "seemore.md"
align: "True"
```

```blocks-button
content: "Go Somewhere"
link: "seemore.md"
align: "True"
```

```blocks-button
content: "Go Somewhere"
link: "seemore.md"
align: "True"
```

## Card

Cards are a great way to grab some attention. Consolidate your content into a compact, stylish representation.

```blocks-card
title: "A Card"
caption: "Look! It's a card!"
image: "./assets/blocks-watermark.png"
button: "Press Me"
link: "introduction.md#card"
```

A maximum of four cards can be displayed on a single row, with other cards wrapping to the next row. Cards which don't take up a full row will automatically be centered on the page. Cards are also responsive, dropping down below the average tablet screen size will vertically stack the contents of the page to fit on smaller screen devices.

### Alignment

Similar to the button component, cards which have the `align: "True"` attribute are placed into a row with a maximum span of four cards per row. Aligned cards get automatically centered in their row with automatic wrapping. 

```blocks-card
title: "A Card"
caption: "Look! It's a card!"
image: "./assets/blocks-watermark.png"
button: "Press Me"
link: "introduction.md#card"
align: "True"
```