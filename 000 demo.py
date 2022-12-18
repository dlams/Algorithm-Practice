from random import sample



### DEFINE GLOBAL ENV
p_x, p_y, p_z = 10, 4, 10

# a_h_x, a_h_y, a_h_z = p_x, p_y, p_z - 3
base_x_loc = p_x - 5
a_h_x = p_x
a_h_y = p_y
a_h_z = p_z - 3

ELEMENTS_SIZE = 11   # 샘플링 갯수
ELEMENTS_START = 523   # 수소원소
ELEMENTS_END = 542  # 칼슘원소
# num_elems = 11
# h = 523
# ca = 542



### 학습용 로봇 관련 함수 정의
# def goto(slot):
#     target_x = base_x_loc + slot - 1
#     agent.teleport(world(target_x, a_h_y, a_h_z - 1), NORTH)

def goto(dx, dy, dz):
    agent.teleport(world(p_x + dx, p_y + dy, p_z + dz), NORTH)

def gohome(loc):
    agent.teleport(loc, NORTH)

def place_element(elm, slot):
    agent.set_slot(slot)
    agent.set_item(elm, 1, slot)
    agent.place(FORWARD)
    agent.set_item(0, 1, slot)

def destroy_element():
    agent.destroy(FORWARD)
    agent.collect_all()
    agent.set_item(0, 1, 1)

def compare(slot_a, slot_b):
    goto(slot_a)
    a_val = agent.inspect(AgentInspection.BLOCK, FORWARD)
    goto(slot_b)
    b_val = agent.inspect(AgentInspection.BLOCK, FORWARD)
    gohome(a_homeLoc)
    return b_val - a_val

def swap(slot_a, slot_b):
    goto(slot_a)
    a_val = agent.inspect(AgentInspection.BLOCK, FORWARD)
    destroy_element()
    goto(slot_b)
    b_val = agent.inspect(AgentInspection.BLOCK, FORWARD)
    destroy_element()
    goto(slot_a)
    place_element(b_val, slot_a)
    goto(slot_b)
    place_element(a_val, slot_b)
    gohome(a_homeLoc)


### EXECUTE FUNC DEFINE
def set_blocks():
    elems = sample(range(ELEMENTS_START, ELEMENTS_END + 1), ELEMENTS_SIZE)
    for dz in range(1, 4 + 1):
        goto(0, 0, dz)
    for dx in range(11):
        goto(dx - 5, 0, 4)
        place_element(elems[dx], 0)

def destroy_blocks():
    for dz in range(1, 4 + 1):
        goto(0, 0, dz)
    for dx in range(11):
        goto(dx - 5, 0, 4)
        place_element(0, 0)

player.on_chat("set", set_blocks)
player.on_chat("clear", destroy_blocks)

# res=compare(4,8)
# player.say(str(res))

player.teleport(world(p_x, p_y, p_z))
agent.teleport(world(a_h_x, a_h_y, a_h_z), NORTH)
a_homeLoc = agent.get_position()










