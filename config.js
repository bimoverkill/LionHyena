var config = {
    food_generation: {
        meat_per_day: 8,
        meat_increase_per_day: 4,
        food_points_per_meat: 2
    },
    behavior: {
        default: {
            icon: "assets/entity.png"
        },
        lion: {
            icon: "assets/lion.png",
            draw_color: {
                r: 255,
                g: 145,
                b: 0
            },
            view_distance: 3,
            minimum_food: 1,
            reproduction: {
                full: 1.5,
                half: 1
            }
        },
        hyena: {
            icon: "assets/hyena.png",
            draw_color: {
                r: 0,
                g: 255,
                b: 0
            },
            view_distance: 3,
            minimum_food: 0.5,
            reproduction: {
                full: 1,
                half: 0.5
            }
        }
    }
}