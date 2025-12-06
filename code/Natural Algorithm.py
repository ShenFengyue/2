import random
import time

class Human:
    def __init__(self, name):
        self.name = name
        self.energy = 100.0       # 认知能量 (意志力)
        self.dopamine = 0.0       # 多巴胺水平 (兴奋度)
        self.skill = 10.0         # 技能/认知水平
        
    def consume(self, content):
        """用户消费内容后的生理反应"""
        self.energy -= content['cost']
        self.dopamine += content['stimulus']
        
        # 多巴胺的自然衰减（模拟生物代谢）
        self.dopamine *= 0.8  
        
        # 只有当 难度 略高于 技能 时，技能才会增长 (心流区：难度 = 技能 + 10%)
        if 0 < content['difficulty'] - self.skill <= 2.0:
            growth = 0.5
            print(f"  ✨ 触发心流！能力提升 +{growth}")
            self.skill += growth
        else:
            print(f"  💨 无效输入 (太简单无聊 或 太难焦虑)")

    def __repr__(self):
        return f"[{self.name}] 🔋精力:{self.energy:.1f} | 💊多巴胺:{self.dopamine:.1f} | 🧠能力:{self.skill:.1f}"

# --- 两种算法的对比 ---

def traditional_recommendation(user, content_pool):
    """
    传统算法：最大化多巴胺 (点击率预估)
    逻辑：只要用户还有一口气，就给他最刺激的东西
    """
    # 简单粗暴：按刺激度排序，永远推最爽的
    return max(content_pool, key=lambda x: x['stimulus'])

def natural_algorithm(user, content_pool):
    """
    🔥 自然算法：生物稳态 + 最近发展区
    逻辑：模拟生物体调节，追求长期存续和增长
    """
    # 1. 体内平衡检查 (Homeostasis Check)
    # 如果多巴胺过高（上头了/成瘾风险），强制推“低刺激”内容进行“拮抗调节”
    if user.dopamine > 20.0:
        print("  ⚠️ 检测到多巴胺过载 (上头风险) -> 启动冷却机制")
        return next(c for c in content_pool if c['type'] == '深度阅读') # 强制降温

    # 2. 能量模型检查 (Energy Model)
    # 如果精力耗尽，推“修复性”内容，而不是继续消耗
    if user.energy < 30.0:
        print("  💤 检测到认知疲劳 -> 启动修复模式")
        return next(c for c in content_pool if c['type'] == '休息冥想')

    # 3. 最近发展区 (Zone of Proximal Development)
    # 在精力充足且清醒时，推“略高于当前能力”的内容，促成进化
    # 寻找难度在 [skill, skill + 3] 之间的内容
    candidates = [c for c in content_pool if user.skill <= c['difficulty'] <= user.skill + 3.0]
    
    if candidates:
        print("  🚀 状态极佳 -> 推荐挑战性任务 (心流)")
        return max(candidates, key=lambda x: x['difficulty']) # 推其中最难的
    else:
        return content_pool[0] # 兜底

# --- 模拟数据 ---

# 内容池：[类型, 消耗精力, 产生多巴胺, 难度系数]
contents = [
    {'type': '短视频',   'cost': 5,  'stimulus': 15, 'difficulty': 1},  # 高刺激，低营养
    {'type': '爽文',     'cost': 8,  'stimulus': 10, 'difficulty': 5},  # 中刺激，低难度
    {'type': '深度阅读', 'cost': 15, 'stimulus': 2,  'difficulty': 12}, # 低刺激，高难度 (一开始读不懂)
    {'type': '休息冥想', 'cost': -20,'stimulus': 0,  'difficulty': 0},  # 恢复精力
    {'type': '高阶课程', 'cost': 20, 'stimulus': 5,  'difficulty': 15}, # 只有能力够了才能学
]

# --- 开始模拟 ---

print("=== 🛑 模拟场景：传统推荐算法 (利用人性) ===")
u1 = Human("用户A")
for i in range(3):
    print(f"\n第 {i+1} 次推荐:")
    rec = traditional_recommendation(u1, contents)
    print(f"  🤖 算法推送: {rec['type']} (意图: 让你爽)")
    u1.consume(rec)
    print(f"  {u1}") 
# 结果预测：用户A会很爽，但能力(skill)完全不长，精力(energy)飞速下降，最终变成废人。

print("\n\n=== 🌱 模拟场景：自然算法 (强化人性) ===")
u2 = Human("用户B (你)")
# 假设用户能力刚好能读懂一点深度阅读
u2.skill = 10.0 

for i in range(5):
    print(f"\n第 {i+1} 次推荐:")
    rec = natural_algorithm(u2, contents)
    print(f"  🌲 算法推送: {rec['type']}")
    u2.consume(rec)
    print(f"  {u2}")
    
    