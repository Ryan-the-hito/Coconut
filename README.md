# 🥥Coconut: Finder-iCloud Photo Synchronizer

![Y5Xt1FR](https://i.imgur.com/EQKrs6L.png)

A menu bar app on macOS to sync local photos in Finder to iCloud. 一个将本地路径下的图片自动同步到 iCloud 的软件。

<p align="center"><a href="https://www.buymeacoffee.com/ryanthehito/e/180273">购买软件（$5）点这里</a></p>

## 解决问题

众所周知，macOS 是一个基于文件的系统，而 iOS 和 iPadOS 是一个基于软件的系统。所以，在 macOS 上就同时有访达储存的图片文件和通过 Photos 储存的照片，两种交互同时存在。在 iOS 和 iPadOS 之间，图片可以通过 iCloud 同步，实现几乎无缝同步多设备的效果。但是对于 macOS，就没那么容易了，虽然照片里的能同步，但是访达里的图片想要同步必须手动导入。从这个角度看，macOS 似乎是同步环节之外的一个小小分支，只有一只脚伸入了 iCloud 组成的同步环中。这本不是一个新问题，在这之前，我已经在少数派等网站上看到过很多方法来同步 macOS 上的图片到其他设备，以期实现完整的 iCloud 同步效果，例如[这篇文章](https://sspai.com/post/79593)就介绍了用 Automator 进行同步的方法。不过我更期待一个全自动的方案，一个不需要用户手动点击即可自动同步的方案，这样才算是一个完整的苹果生态链体验。于是，我就写了 Coconut 这个软件。

当然，这个软件的思路和 [Mango](https://github.com/Ryan-the-hito/Mango)是类似的，Coconut 通过定期遍历本地文件列表再导入可同步的 Photos。我写完 Mango 之后就用同样的思路写了 Coconut。

## 功能亮点

![1](https://i.imgur.com/3luG6HM.png)

### Coconut 的唯一功能就是定时检测特定路径，然后将其中的照片导入 Photos 这个自带 APP

Coconut 首先有一个定时功能，表示每隔多久检测一次特定的路径（至少是一分钟），是否有新照片。如果有新照片，那么就会触发导入的动作，在确保导入完成之后将改照片移入该路径下名为“CoconutDone”的文件夹内。

因此这里有一个需要注意的地方：macOS 是一个两种图片处理逻辑并存的中心，Coconut 并不希望用户将所有图片按照照片的顺序结构导入云端，所以只允许对单一一个路径下的图片操作，避免把大量不必同步的图片自动同步到云端。另外，这个路径里也只能存入可以导入 Photos 的图片各式。文本、PDF 等格式无法被导入照片库，因此也无法被 Coconut 处理。

**因此，推荐用户在设置中将路径设为截图（无论是自带还是第三方）的本地存储路径。**

另外，因为导入后需要同步，因此 Coconut 在使用过程中需要 Photos 软件始终在后台。唯其如此才能实现文首提出的效果。如此设置不是只能导入截图。如果想要把其他图片导入怎么办呢？也不难，使用一些第三方的快捷方式，例如在任务栏内显示访达路径，可以快速地将需要同步的图片移动到对应路径下，然后用户只需要静静等待同步完成即可在手机上也看到了。（这一设计在后续还会跟进，会考虑是否通过剪贴板同步，但是这显得有些没必要，因为 Airdrop 就能完成。因此在目前的版本里没有这样做。）

最后，需要考虑的一点是，因为同步有时间限制，最低检测间隔是一分钟，那么导入必须在一分钟内完成。为此，Coconut 一次性最多导入五张图片。如果用户有上百上千张照片，显然是不适合用 Coconut 来导入的。**准确来说，Coconut 适用于日常使用情景，尤其是希望截图可以无感知地自动同步到各个设备以供使用。**

### 保护隐私、离线使用、同步协同

除了功能问题，还有一个审美问题摆在我们面前，那就是：都能实现同样的功能，到底要一个怎样的软件才好呢？我希望能有一个本身离线的工具，保证不会读取和上传我的图片，同时我又希望这样的工具可以帮我实现同步协同的问题，最好不用我多费力气，也不需要我动动指头去手动操作。如果你和我有相同的软件使用审美，说不定 Coconut 也非常适合你！Coconut 就是在这样的思路下创作的软件，只是一系列本地操作的集合，而不需要任何线上服务。如果你断网使用它，也是完全可行的。（不过不能影响到 Photos 这个软件，如果给 Photos 软件断网就没法同步了……以及，检查更新还是需要联网的。这是唯一需要网络的地方）Coconut 是一个开源软件，可供检视其中的代码。

## 环境要求

- MacOS 11 以上（测试环境为 MacOS 13.6.1）；
- M 系列芯片；
- Coconut 完全不会读取您的照片，也不会有任何上传行为。但是检查更新需要您的网络能连接到 GitHub，所以网络环境需要您自理。

## 类型价目

Coconut 是付费软件，只需 $5，可以点击[这个连接](https://www.buymeacoffee.com/ryanthehito/e/180273)购买。如果你对我的其他软件感兴趣，也可以来看看，很多软件都是免费的，例如 [Mango](https://github.com/Ryan-the-hito/Mango)、[Broccoli](https://github.com/Ryan-the-hito/Coconut)等。

## 下载安装

从 [Releases](https://github.com/Ryan-the-hito/Coconut/releases) 中购买，然后下载最新版本，接着将解压后的 .app 文件拖入程序文件夹。

## 使用说明

### 打开时

<p align="center">
  <img src="https://i.imgur.com/hmeMYKc.png" width=300 />
  <img src="https://i.imgur.com/Rz1Iok8.png" width=300 />
</p>

Coconut 是一个全任务栏软件，打开时会在任务栏中显示图标。在第一次打开时，如果遇见打不开的情况，说软件损坏，这其实是一个非常普遍也非常容易解决的问题。因为本软件没有苹果的证书，所以它会有这样的提示。要绕过检查，只需在终端里输入“sudo xattr -r -d com.apple.quarantine /Applications/Coconut.app”，按提示输入开机密码即可。

上图中左边的是读取文件夹提示，因为 Coconut 需要遍历文件路径下的图片。实际上每次运行这个弹窗都会出现，所以建议用户在 Privacy & Security 下面的 Full Disk Access 添加 Coconut。

上图右边的是对 Photos 这各软件操作的许可，如需成功完成次操作，需要用户去 System Settings 里面，在 Privacy & Security 下面的 Accessibility，把 Coconut 添加进来。

有了这两个允许之后，同意上述弹窗，即可开始使用 Coconut。使用时，先打开 Settings 窗口加入个性化的配置，然后出来，点击“Switch on Coconut!”，菜单前面显示一个小勾，即表明 Coconut 已经在后台运作。如果不想继续使用，再点一次即可取消。

### 更新时

与安装是一样的，只是不要忘了 macOS 上更新需要给这个软件重新设置一遍安全权限。

## 注意事项

<p align="center">
  <img src="https://i.imgur.com/0urAk9g.png" width=400 />
</p>

根据苹果的解释，勾上这个选项的意思是，导入 Photos 的图片会单独保留一个副本，而取消则意味着 Photos 仅仅用来展示，只保留了一个路径。我建议把这个选上。

## Q&A

如果遇到任何特殊情况，请访问 **[Q&A](https://github.com/Ryan-the-hito/Q-A)❓** 查看是否有现成的解决方案，或进一步联系我。

## 证书信息

GPL-3.0 license

## 特别致谢

1. [Qt](https://github.com/qt)：本软件遵循 Qt 的开源协议。

## 支持作者

[Buy Me a Cup of Coffee](https://www.buymeacoffee.com/ryanthehito)

<p align="center">
  <img src="https://i.imgur.com/OHHJD4y.png" width=240 />
  <img src="https://i.imgur.com/6XiKMAK.png" width=240 />
</p>
