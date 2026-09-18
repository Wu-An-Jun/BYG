# G4-COMBO-1统一讲评｜23/30

6个计算项：4、4、4、2、4、5分。除3A外，5项主体结果正确，但4个已完成不定积分漏+C。第3A尚未形成结果，不把它说成第5个正确原函数。

## 基本积分与换元

1. $x^4-3\ln|x|+2\sin x+C$。没有x>0限制，应保留绝对值。
2A. $\frac12\ln(x^2+4)+C$。
2B. $\frac14e^{2x^2}+C$。
3B. $x\ln x-x+C$（x>0）。
4. $e-1$，定积分不加C。此题讲义中给过，不能只凭它宣称未见题迁移。

你的d(x²)思路合法：d(x²)=2x dx。因此(1/2)∫e^(2x²)d(x²)确实得到(1/4)e^(2x²)。写d(x²)，不要省括号使人误读为(dx)²。

## 分部A：合法选择、低效选择与公式错误要分开

你取u=cos2x、dv=x dx，是合法拆分；但du=−2sin2x dx，不能漏链式2及dx。

分部来自$d(uv)=u\,dv+v\,du$，所以：
$$\int u\,dv=uv-\int v\,du.$$

你的余项$\int\cos(2x)d(x^2/2)$实际上仍是$\int u\,dv$，不是$\int v\,du$。

原选择若用对公式会得到：
$$I=\frac{x^2}{2}\cos2x+\int x^2\sin2x\,dx,$$
反而更复杂，所以建议换选择，而不是说原选择不合法。

高效选择：
$$u=x,\quad dv=\cos2x\,dx,\quad du=dx,\quad v=\frac12\sin2x.$$
$$I=\frac{x}{2}\sin2x-\frac12\int\sin2x\,dx
=\boxed{\frac{x}{2}\sin2x+\frac14\cos2x+C}.$$

核验：导数中sin2x/2和−sin2x/2抵消，剩x cos2x。

## ln x那题实际上已用对角色

u=lnx、dv=dx、du=dx/x、v=x；余项∫x dlnx=∫dx。主体结果对，只需完整微分记号与+C。

不用整组重做。下一次一次交[[G4-PARTS-FIX-分部积分修复练习]]两道完整过程，检查u/dv选择、du系数、v du以及+C。再决定进入下一积分类型还是补一个共性错。
