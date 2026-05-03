"""
Knowledge Base - Standards Retrieval
规范知识库 - 基于向量检索的规范文档管理
"""

from pathlib import Path
from typing import Dict, List


class StandardsKnowledgeBase:
    """规范知识库"""
    
    def __init__(self, standards_dir: str = "docs/standards"):
        self.standards_dir = Path(standards_dir)
        self.standards_cache = {}
        self._load_standards()
    
    def _load_standards(self):
        """加载所有规范文档"""
        if not self.standards_dir.exists():
            self.standards_dir.mkdir(parents=True, exist_ok=True)
            self._create_default_standards()
        
        # TODO: 集成向量数据库进行语义检索
        # 当前使用简单的文件缓存
        
        for category_dir in self.standards_dir.iterdir():
            if category_dir.is_dir():
                category = category_dir.name
                self.standards_cache[category] = []
                
                for md_file in category_dir.glob("*.md"):
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        self.standards_cache[category].append({
                            "file": md_file.name,
                            "content": content[:500],  # 只取前500字符作为示例
                            "path": str(md_file)
                        })
    
    def _create_default_standards(self):
        """创建默认规范文档"""
        
        # Coding Standards
        coding_dir = self.standards_dir / "coding_standards"
        coding_dir.mkdir(exist_ok=True)
        
        (coding_dir / "python_style.md").write_text(
            "# Python Coding Standards\n\n"
            "## PEP 8 Compliance\n"
            "- Use 4 spaces for indentation\n"
            "- Limit lines to 79 characters\n"
            "- Use snake_case for functions and variables\n"
            "- Use CamelCase for classes\n",
            encoding='utf-8'
        )
        
        # Development Guidelines
        dev_dir = self.standards_dir / "development_guidelines"
        dev_dir.mkdir(exist_ok=True)
        
        (dev_dir / "architecture_patterns.md").write_text(
            "# Architecture Patterns\n\n"
            "## Recommended Patterns\n"
            "- Layered Architecture for web applications\n"
            "- Repository Pattern for data access\n"
            "- Dependency Injection for testability\n",
            encoding='utf-8'
        )
        
        (dev_dir / "security_requirements.md").write_text(
            "# Security Requirements\n\n"
            "## Must Follow\n"
            "- Validate all inputs\n"
            "- Use parameterized queries\n"
            "- Implement proper authentication\n"
            "- Encrypt sensitive data\n",
            encoding='utf-8'
        )
    
    def retrieve_relevant_standards(
        self,
        query: str,
        categories: List[str] = None,
        top_k: int = 3
    ) -> List[Dict]:
        """
        检索相关规范
        
        Args:
            query: 查询文本
            categories: 过滤类别
            top_k: 返回数量
            
        Returns:
            相关规范列表
        """
        results = []
        
        # TODO: 实现真正的语义检索
        # 当前返回所有规范的摘要
        
        for category, standards in self.standards_cache.items():
            if categories and category not in categories:
                continue
            
            for standard in standards[:top_k]:
                results.append({
                    "category": category,
                    "file": standard["file"],
                    "preview": standard["content"],
                    "relevance_score": 0.8  # Placeholder
                })
        
        return results[:top_k * 2]
    
    def add_standard(self, category: str, filename: str, content: str):
        """添加新规范"""
        category_dir = self.standards_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = category_dir / filename
        filepath.write_text(content, encoding='utf-8')
        
        # Update cache
        if category not in self.standards_cache:
            self.standards_cache[category] = []
        
        self.standards_cache[category].append({
            "file": filename,
            "content": content[:500],
            "path": str(filepath)
        })
