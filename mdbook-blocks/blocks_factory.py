import blocks_components as blocks

def blocks_factory(component_name):

    # Add new components here
    component = {
        'alert': blocks.BlocksAlert,
        'card': blocks.BlocksCard,
        'badge': blocks.BlocksBadge,
        'button': blocks.BlocksButton
    }

    return component[component_name]